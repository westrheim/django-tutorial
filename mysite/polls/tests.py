from django.test import TestCase, Client

# Create your tests here.
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question



class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date 
        is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes = 59, seconds = 59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class ViewsTests(TestCase):

    def test_page_load_polls_index(self):
        """
        the polls index page should load
        """
        client = Client()
        response = client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
