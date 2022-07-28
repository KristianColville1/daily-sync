from django.shortcuts import render
from django.views import View, generic
from posts.models import Post
class FeedView(View):
    """
    FeedView class
    """
    def get(self, request, *args, **kwargs):
        test = Post.objects.filter(status=1)
        test2 = Post.objects.filter(status=1)
        events = []
        events.extend(test)
        events.extend(test2)
        events = list(dict.fromkeys(events))
        return render(request, 'feed/index.html', {'events': events})
    
