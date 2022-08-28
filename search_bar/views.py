from django.shortcuts import render
from itertools import chain
from django.views.generic import ListView
from django.db.models import Q
from profiles.models import Profile
from posts.models import Post, Comment


class SearchView(ListView):
    """
    Search View class to view querysets
    """
    model = Profile
    template_name = 'search_bar/search.html'
    paginate_by = 16
    
    def get_queryset(self):
        """
        Searches for objects from the user input
        """
        request = self.request
        query = request.GET.get('q', None)
        object_list = ''
        if query is not None:
            object_list = Profile.objects.filter(
                Q(first_name__in=query) | Q(last_name__in=query)
            )
        return object_list
        
