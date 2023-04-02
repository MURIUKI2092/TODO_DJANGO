from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
#filters for searching
from rest_framework import permissions,filters
from todos.models import Todo
#DjangoFilterBackend for filtering
from django_filters.rest_framework import DjangoFilterBackend
from todos.pagination import CustomPagination
# Create your views here.


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    #permission classes ie; one must be authenticated
    permission_classes = (IsAuthenticated,)
    pagination_classes = CustomPagination
    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields =['id', 'title','description', 'is_complete']
    search_fields =['id', 'title','description', 'is_complete']
    ordering_backends =['id', 'title','desc', 'is_complete']
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
    