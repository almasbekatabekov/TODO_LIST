from django.shortcuts import render
from rest_framework.views import Response, APIView
# Create your views here.
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPermission


class ListTodoView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission, )

class DetailTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission, )    