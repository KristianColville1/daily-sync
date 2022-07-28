from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))


class Post(models.Model):
    """
  Post model
  """
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="user_posts")
    title = models.TextField(max_length=200, unique=True)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User,
                                   related_name='liked_posts',
                                   blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField()
    type = "post"

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
