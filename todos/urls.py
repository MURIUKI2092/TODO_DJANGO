from todos.views import TodosApiView,TodoDetailAPIView
from django.urls import path


urlpatterns = [
    path('', TodosApiView.as_view(), name="todos"),
    path('<uuid:todo_uuid>', TodoDetailAPIView.as_view(), name="todo")
]
