from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
  Creates a form object for the post model
  """

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )
        widgets = {
            'title':
            forms.Textarea(attrs={
                'rows': 1,
                'placeholder': 'Write the title of your post here'
            }),
            'content':
            forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Write your post here'
            })
        }


class CommentForm(forms.ModelForm):
    """
  Creates a form object for the comment model
  """

    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content':
            forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here'
            })
        }
