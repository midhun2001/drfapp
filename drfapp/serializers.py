from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    role = serializers.CharField(max_length=255, required=False, default='admin')
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)


class AssociationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    info = serializers.CharField(max_length=255)
    membership_fees = serializers.DecimalField(max_digits=10, decimal_places=2)
    address = serializers.CharField(max_length=255)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    admin = serializers.IntegerField()
