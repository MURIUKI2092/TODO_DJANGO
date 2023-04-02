from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo
# Create your tests here.

class TestApiTestCase(APITestCase):
    
    def create_todo(self):
        sample_todo ={'title':"hello", 'description':"test"}
        response =self.client.post(reverse('todos'),sample_todo)
        return response
        
    def authenticate(self):
        #to get the bearer token for the user need to register the user, log in the user to obtain it
        self.client.post(reverse('register'),{
            'username':"username","email":"email@gmail.com","password":"password"
        })
        response = self.client.post(reverse('Login'),{"email":"email@gmail.com","password":"password"})
        print("++++++++",response)
        #get the refresh token to log in user
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']['refresh_token']}")
    
class TestListCreateTodos(TestApiTestCase):
    
   
    def test_should_not_create_todos_without_an_authenticated_user(self):
        response =self.create_todo()
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
    def test_should_create_a_single_todo(self):
        #tests whether it reaches the db
        prev_todo_count = Todo.objects.all().count()
        self.authenticate()
        
        response =self.create_todo()
        self.assertEqual(Todo.objects.all().count(),prev_todo_count+1)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['description'],'test')
        self.assertEqual(response.data['title'],'hello')

    def test_that_retrieves_all_todos(self):
        self.authenticate()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'],list)

        self.create_todo()
        
        res = self.client.get(reverse('todos'))
        self.assertIsInstance(res.data['count'],int)
        self.assertEquals(res.data['count'],1)
        
class TestTodoDetailAPIView(TestApiTestCase):
    def test_retrieves_one_todo(self):
        self.authenticate()
        response = self.create_todo()
        print(response.data,">>>>>>>")
        res = self.client.get(reverse("todo",kwargs={"todo_uuid":response.data["todo_uuid"]}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        todo = Todo.objects.get(todo_uuid=response.data["todo_uuid"])
        
        self.assertEqual(todo.title, res.data['title'])
    
    def test_updates_one_todo(self):
        self.authenticate()
        response=self.create_todo()
        
        res = self.client.patch(reverse('todo',kwargs ={'todo_uuid':response.data["todo_uuid"]}),{
            "title":"new Title", 'is_complete':True
        })
        todo = Todo.objects.get(todo_uuid=response.data["todo_uuid"])
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(todo.is_complete,True)
        self.assertEqual(todo.title,"new Title")
        
    def test_deletes_one_todo(self):
        self.authenticate()
        response=self.create_todo()
        prev_db_count = Todo.objects.all().count()
        self.assertEqual(prev_db_count,1)
        res = self.client.delete(reverse("todo",kwargs={"todo_uuid":response.data["todo_uuid"]}))
        self.assertEqual(res.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.all().count(),prev_db_count-1)