from email.policy import default
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from posts.models import Post


class Profile(models.Model):
    """
    Profile model
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=320, unique=True)
    d_o_b = models.DateField(blank=True, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profiles')
    avatar = CloudinaryField('avatar', folder='user_avatars', null=True, blank=True, default='/static/img/default-profile-image.png')
    posts = models.ManyToManyField(Post, related_name="user_posts")
    friends = models.ManyToManyField('self', blank=True, related_name='user_friends')
    bio = models.TextField(max_length=800, unique=False)
    profile_slug = AutoSlugField(populate_from=username, unique=True)

    def __str__(self):
        return self.username
