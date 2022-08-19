from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileOwnerView.as_view(), name='profile'),
    path('view_profile/<slug:slug>/',
         views.OtherProfileView.as_view(),
         name='view_profile'),
    path('follow_profile/<int:profile_id>/',
         views.follow_profile,
         name='follow'),
    path('user_profiles/',
         views.AllProfilesView.as_view(),
         name='user_profiles'),
]
