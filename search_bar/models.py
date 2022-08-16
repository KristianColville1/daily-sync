from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class SearchModel(models.Model):
    """
    Search model to store user searches
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="searches",
                             null=True)
    searches = ArrayField(models.models.CharField(max_length=30, blank=True))
