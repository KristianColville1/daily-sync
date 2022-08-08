from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Profile model
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=320, unique=True)
    d_o_b = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=200, unique=False)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profiles')
    avatar = CloudinaryField('avatar',
                             folder='avatars',
                             null=True,
                             blank=True,
                             default='/static/img/default-profile-image.png')
    friends = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=True,
                                     related_name='friends')
    follows = models.ManyToManyField('self',
                                     blank=True,
                                     symmetrical=False,
                                     related_name='follows')

    def __str__(self):
        return self.user.username
