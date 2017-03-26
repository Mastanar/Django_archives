from django.views import generic
from feedjack.models import Post

class IndexView(generic.ListView):
    template_name = 'feeding/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        return Post.objects.order_by('-date_modified')[:10]

class DetailView(generic.DeleteView):
    model = Post
    template_name = 'feeding/detail.html'
    context_object_name = 'news'
