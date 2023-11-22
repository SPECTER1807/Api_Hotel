from django.test import TestCase
from .models import Usuario

class UsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            password='hashed_password'
        )

    def test_str_method(self):
        usuario = Usuario.objects.get(email='john.doe@example.com')
        self.assertEqual(str(usuario), 'John Doe')

    def test_unique_email_constraint(self):
        with self.assertRaises(Exception):
            Usuario.objects.create(
                first_name='Jane',
                last_name='Doe',
                email='john.doe@example.com',
                password='hashed_password'
            )

    def test_model_fields(self):
        usuario = Usuario.objects.get(email='john.doe@example.com')
        self.assertEqual(usuario.first_name, 'John')
        self.assertEqual(usuario.last_name, 'Doe')
        self.assertEqual(usuario.email, 'john.doe@example.com')
        self.assertEqual(usuario.password, 'hashed_password')  # En una aplicación real, deberías cifrar la contraseña