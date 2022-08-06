from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts, name='posts'),
    path('delete/<int:post_id>/',
         views.delete_post,
         name='delete_post')
]
