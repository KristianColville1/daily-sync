from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedViewIndex.as_view(), name='feed'),
    path("<slug:slug>/", views.FeedViewPost.as_view(), name='view_post'),
]
