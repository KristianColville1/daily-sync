from django.shortcuts import render
from itertools import chain
from django.views.generic import ListView
from django.db.models import Q
from profiles.models import Profile
from posts.models import Post, Comment


class SearchView(ListView):
    """
    Search function view to view search results
    """
    template_name = 'search_bar/search.html'
    paginate_by = 25
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
    
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        return Post.objects.none()
