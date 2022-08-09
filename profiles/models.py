from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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
                             folder='avatars',
                             null=True,
                             blank=True)
    friends = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=True,
                                     related_name='user_friends')
    follows = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=False,
                                     related_name='user_followers')
    slug = AutoSlugField(populate_from="user", unique=True)

    def __str__(self):
        return self.user.username

    @property
    def get_avatar(self):
        """
        Returns a default user image or the users avatar
        """
        if self.avatar:
            return self.avatar.url
        return '/static/img/default-profile-image.png'


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.email = instance.email
        user_profile.save()


post_save.connect(create_profile, sender=User)
