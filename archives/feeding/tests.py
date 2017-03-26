import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from feedjack.models import Feed, Post

def create_post(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    feed = Feed(feed_url='127.0.0.1:8000', name='test', shortname='show')
    feed.save()
    return Post.objects.create(feed=feed, title=text, date_modified=time)

class QuestionViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('feeding:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No feeding are available.")
        self.assertQuerysetEqual(response.context['latest_news_list'],[])

    def test_detail_view_with_not_text(self):
        url = reverse('feeding:detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_text(self):
        past_text = create_post(text='Try do it.', days=-5)
        url = reverse('feeding:detail', args=(past_text.id,))
        response = self.client.get(url)
        self.assertContains(response, past_text.title)
        self.assertEqual(response.status_code, 200)
