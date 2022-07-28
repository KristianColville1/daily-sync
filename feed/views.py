from django.shortcuts import render
from django.views import View, generic
from posts.models import Post

class FeedView(generic.View):
    """
    FeedView class
    """
    template_name = 'feed/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'feed/index.html')

    def list_feed_posts(request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'feed/index.html', context)
