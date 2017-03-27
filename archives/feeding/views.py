from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from feedjack.models import Post

class IndexView(generic.ListView):
    model = Post
    paginate_by = 4
    template_name = 'feeding/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-date_modified')

class DetailView(generic.DeleteView):
    model = Post
    template_name = 'feeding/detail.html'
    context_object_name = 'news'
