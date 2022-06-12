import datetime

from django.contrib.auth.models import User
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
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time, published_by=user)
        future_question.save()
        self.assertIs(future_question.was_published_recently(), False)
        self.assertEqual(future_question.published_by, user)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
