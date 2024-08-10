from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from .serializers import AssociationSerializer, UserSerializer


class UserListCreateView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, role, username FROM users")
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append({
                    'id': row[0],
                    'role': row[1],
                    'username': row[2],
                })
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Insert into the users table using raw SQL
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "INSERT INTO users (role, username, password) VALUES (%s, %s, %s) RETURNING id",
                        [data.get('role', 'admin'), data['username'], data['password']]
                    )
                    user_id = cursor.fetchone()[0]
                    return Response({'id': user_id, 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssociationListCreateView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM association")
            rows = cursor.fetchall()
            associations = []
            for row in rows:
                associations.append({
                    'id': row[0],
                    'name': row[1],
                    'info': row[2],
                    'membership_fees': row[3],
                    'address': row[4],
                    'latitude': row[5],
                    'longitude': row[6],
                    'admin': row[7],
                })
        serializer = AssociationSerializer(associations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssociationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "INSERT INTO association (name, info, membership_fees, address, latitude, longitude, admin) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        [data['name'], data['info'], data['membership_fees'], data['address'], data['latitude'], data['longitude'], data['admin']]
                    )
                    return Response({'message': 'Association created successfully'}, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
