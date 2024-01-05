from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model() # noqa
        user = User.objects.create_user(email="yazdan@dev.dev", password="test_password")
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, "yazdan@dev.dev")
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="test_case")

    def test_create_superuser(self):
        User = get_user_model() # noqa
        user = User.objects.create_superuser(email="ayazdan@dev.dev", password="test_password")
        self.assertEqual(user.email, "ayazdan@dev.dev")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="",
                password="test_case",
                is_superuser=False
            )

