from django.test import TestCase
from django.urls import reverse


class BrewingPageTests(TestCase):
    def test_brewing_method_list_page_loads(self):
        response = self.client.get(reverse("brewing:method_list"))
        self.assertEqual(response.status_code, 200)
