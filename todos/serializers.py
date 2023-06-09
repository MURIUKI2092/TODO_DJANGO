#so as to do crud operations
from rest_framework.serializers import ModelSerializer
from todos.models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields=("id","todo_uuid","title", "description","is_complete")
