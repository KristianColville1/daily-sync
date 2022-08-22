from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.FeedViewIndex.as_view()), name='feed'),
    path("<slug:slug>/", login_required(views.FeedViewPost.as_view()), name='view_post'),
]
