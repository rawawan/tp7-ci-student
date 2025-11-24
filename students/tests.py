from django.test import TestCase
from django.contrib.auth.models import User

class SimpleTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="pass1234")

        # Vérifier que l'utilisateur existe bien
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, "testuser")
