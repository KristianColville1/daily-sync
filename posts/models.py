from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timesince

STATUS = ((0, "Draft"), (1, "Posted"))


class Post(models.Model):
    """
    Post model
    """
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts",
                               null=True)
    post_body = models.TextField(max_length=500)
    slug = AutoSlugField(populate_from="post_body", unique_with="author")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    total_likes = models.ManyToManyField(User,
                                         related_name="post_likes",
                                         blank=True)
    thumbs_likes = models.ManyToManyField(User,
                                          related_name="thumb_likes",
                                          blank=True)
    heart_likes = models.ManyToManyField(User,
                                         related_name="heart_likes",
                                         blank=True)
    laugh_likes = models.ManyToManyField(User,
                                         related_name="laugh_likes",
                                         blank=True)
    angry_likes = models.ManyToManyField(User,
                                         related_name="angry_likes",
                                         blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    shared = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        String representation
        """
        return self.title

    def count_likes(self):
        """
        Counts the amount of likes a post has
        """
        if self.total_likes.count() > 0:
            return self.total_likes.count()
        return ''

    def count_comments(self):
        """
        Counts the amount of comments a post has
        """
        if self.comments.count() > 0:
            return self.comments.count()
        return ''

    @property
    def calc_time_since(self):
        """
        returns the time since posted in an easy to read format for users
        """
        time_string = timesince.timesince(self.created_on)
        time_options = [
            'minute',
            'hour',
            'day',
            'week',
            'month',
            'year',
        ]
        if time_string[0] != '0':
            for value in time_options:
                amount_to_cut = len(value)
                if value in time_string:
                    index = time_string.index(value)
                    first = time_string[0:index]
                    cut_piece = time_string[index:index + amount_to_cut]
                    last = time_string[index + amount_to_cut - 1]
                    char_1 = cut_piece[0]
                    if last == 'e':
                        time_string = first + char_1 + 'ins'
                    else:
                        time_string = first + char_1 + last + 's'
        return time_string


class Comment(models.Model):
    """
    Comment model class
    """
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    contributor = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="comments",
                                    null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    total_likes = models.ManyToManyField(User,
                                         related_name="comment_likes",
                                         blank=True)
    thumbs_likes = models.ManyToManyField(User,
                                          related_name="comment_thumb_likes",
                                          blank=True)
    heart_likes = models.ManyToManyField(User,
                                         related_name="comment_heart_likes",
                                         blank=True)
    laugh_likes = models.ManyToManyField(User,
                                         related_name="comment_laugh_likes",
                                         blank=True)
    angry_likes = models.ManyToManyField(User,
                                         related_name="comment_angry_likes",
                                         blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

    def count_likes(self):
        if self.total_likes.count() > 0:
            return self.total_likes.count()
        return ''
