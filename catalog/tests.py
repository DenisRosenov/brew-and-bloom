from django.test import TestCase
from django.urls import reverse


class CatalogPageTests(TestCase):
    def test_coffee_list_page_loads(self):
        response = self.client.get(reverse("catalog:coffee_list"))
        self.assertEqual(response.status_code, 200)

    def test_flavor_list_page_loads(self):
        response = self.client.get(reverse("catalog:flavor_list"))
        self.assertEqual(response.status_code, 200)
