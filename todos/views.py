from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
# Create your views here.


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    #permission classes ie; one must be authenticated
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
        
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
