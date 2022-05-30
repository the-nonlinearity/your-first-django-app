from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_index(self):
        """
        Test the index page.
        """
        response = self.client.get(reverse('polls:index'))
        assert response.status_code == 200
