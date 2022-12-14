from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField


class Profile(models.Model):
    """
    Profile model
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=320, unique=True)
    d_o_b = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, unique=False)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    avatar = CloudinaryField('avatar',
                             default='/static/img/default-profile-image.png')
    background = CloudinaryField(
        'background', default='/static/img/default_backgrounds/bg.webp')
    friends = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=True,
                                     related_name='user_friends')
    follows = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=False,
                                     related_name='user_followers')
    slug = AutoSlugField(populate_from="user", unique=True)
    
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.user.username


class FriendRequest(models.Model):
    """
    FriendRequest model
    """
    from_user = models.ForeignKey(User,
                                  related_name="from_user",
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,
                                related_name="to_user",
                                on_delete=models.CASCADE)
    not_accepted = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for a user on sign up to connect everything
    together.
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.email = instance.email
        user_profile.save()
