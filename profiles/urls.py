from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.ProfileOwnerView.as_view()), name='profile'),
    path('view_profile/<slug:slug>/',
         login_required(views.OtherProfileView.as_view()),
         name='view_profile'),
    path('follow_profile/<int:profile_id>/',
         login_required(views.follow_profile),
         name='follow'),
    path('user_profiles/',
         login_required(views.AllProfilesView.as_view()),
         name='user_profiles'),
]
