from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Todo

class TodoAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_todo(self):
        data = {'title': 'Test To-Do'}
        response = self.client.post('/api/todos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test To-Do')

    def test_get_todos(self):
        Todo.objects.create(title='Test To-Do', user=self.user)
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        todo = Todo.objects.create(title='Test To-Do', user=self.user)
        data = {'title': 'Updated To-Do'}
        response = self.client.put(f'/api/todos/{todo.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.get().title, 'Updated To-Do')

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test To-Do', user=self.user)
        response = self.client.delete(f'/api/todos/{todo.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
