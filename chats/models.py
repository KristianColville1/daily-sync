from django.db import models
from django.contrib.auth.models import User

class Chat(models):
    """
    Chat model
    """
    content = models.CharField(max_length=1400)
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)