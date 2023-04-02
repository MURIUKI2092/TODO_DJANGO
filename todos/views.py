from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from rest_framework import response,status
# Create your views here.


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    #permission classes ie; one must be authenticated
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
        
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "todo_uuid"
    
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
    