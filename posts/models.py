from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))


class Post(models.Model):
    """
    Post model
    """
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts",
                               null=True)
    title = models.TextField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique_with="author")
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        return ''

    def count_comments(self):
        if self.comments.count() > 0:
            return self.comments.count()
        return ''


class Comment(models.Model):
    """
    Comment model class
    """
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    contributer = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="comments",
                                    null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        return ''
