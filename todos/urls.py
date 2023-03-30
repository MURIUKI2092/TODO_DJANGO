from todos.views import TodosApiView
from django.urls import path


urlpatterns = [
    path('', TodosApiView.as_view(), name="todo")
]
