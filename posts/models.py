from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))


class Post(models.Model):
    """
    Post model
    """
    slug = models.SlugField(max_length=200, auto_created=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="user_posts",
                               null=True)
    title = models.TextField(max_length=200, unique=True)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        return ''


class Comment(models.Model):
    """
    Comment model class
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User,
                                   related_name='comment_likes',
                                   blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        return ''
