from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase

from polls.models import Poll
# Create your tests here.

class PollMethodTests(TestCase):
    def test_was_publisted_recently_with_future_poll(self):
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEquals(future_poll.was_published_recently(), False)

