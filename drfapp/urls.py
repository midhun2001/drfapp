from django.urls import path
from .views import AssociationListCreateView, UserListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('associations/', AssociationListCreateView.as_view(), name='association-list-create'),
]
