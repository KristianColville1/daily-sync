from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('share_post/<int:post_id>/', views.share_post, name='share_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('create_comment/<int:post_id>/',
         views.create_comment,
         name='create_comment'),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:comment_id>/',
         views.edit_comment,
         name='edit_comment'),
    path('like_post/<int:post_id>/<str:emoji>/',
         views.like_post,
         name='like_post_emoji'),
    path('like_comment/<int:comment_id>/<str:emoji>/',
         views.like_comment,
         name='like_post'),

]
