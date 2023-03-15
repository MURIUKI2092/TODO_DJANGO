from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user('james','maina@gmail.com','password012')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'maina@gmail.com')
        
    def test_create_super_user(self):
        user = User.objects.create_superuser('james','maina@gmail.com','password012')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'maina@gmail.com')
    
    def test_raises_error_if_user_name_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user ,username="",email='maina@gmail.com',password='password012')
        self.assertRaisesMessage(ValueError,"The given username must be set")
        
    def test_raises_error_if_email_is_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="james",email='',password='password012')
        self.assertRaisesMessage(ValueError,"The email must be given")
        
    def test_raises_error_with_message_when_no_user_name_is_provided(self):
        with self.assertRaisesMessage(ValueError,"The given username must be set"):
            user = User.objects.create_user(username='',email='maina@gmail.com',password='password012')
    
    def test_raises_error_with_message_when_no_email_is_provided(self):
        with self.assertRaisesMessage(ValueError,"The email must be given"):
            user = User.objects.create_user(username='james',email='',password='password012')
            
    def test_super_user_status(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have is_staff=True."):
            User.objects.create_superuser(username='james',email='maina@gmail.com',password='password012',is_staff=False)
    
    def test_super_user_is_super_user(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have is_superuser=True."):
            User.objects.create_superuser(username='james',email='maina@gmail.com',password='password012',is_superuser=False)