from django.test import TestCase
from django.urls import reverse


class RecipePageTests(TestCase):
    def test_recipe_list_page_loads(self):
        response = self.client.get(reverse("recipes:recipe_list"))
        self.assertEqual(response.status_code, 200)