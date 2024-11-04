import json
from django.test import TestCase
from .models import Provincia

class PublicationTestCase(TestCase):
    def setUp(self):
        # Cargar los datos JSON
        with open('provincias.json', 'r') as file:
            self.data = json.load(file)

    def test_insert_publications(self):
        for item in self.data['nombre']:
            Provincia = Provincia.objects.create(
                nombre=item
            )
            self.assertIsNotNone(Provincia.id)

        # Verificar que se insertaron todos los registros
        self.assertEqual(Provincia.objects.count(), len(self.data))

