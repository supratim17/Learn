import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30, minutes=10)
        future_question = Question(pub_date=time)
        ago = int(future_question.diff().split()[0])
        self.assertEqual(ago>=0, True)