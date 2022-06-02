import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class IndexViewTests(TestCase):
    def test_index(self):
        """
        Test the index page.
        """
        response = self.client.get(reverse('polls:index'))
        assert response.status_code == 200


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
