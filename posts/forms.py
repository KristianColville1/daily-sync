from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  """
  Creates a form object for the post model
  """
  class Meta:
    model = Post
    fields = ['title', 'content']
  