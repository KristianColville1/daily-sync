from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  """
  Creates a form object for the post model
  """
  class Meta:
    model = Post
    fields = ('title', 'content',)
    widgets = {
      'title': forms.Textarea(attrs={
        'rows': 1,
        'placeholder': 'Write the title of your post here'
      }),
      'content': forms.Textarea(attrs={
        'rows': 6,
        'placeholder': 'Write your post here'
      })
    }  