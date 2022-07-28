from django.urls import path
from . import views
from .views import FeedView

urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
]