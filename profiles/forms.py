from django import forms
from cloudinary.forms import CloudinaryFileField 

from .models import Profile

class EditProfileForm(forms.ModelForm):
    """
    Creates a form object for the profile model
    """

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'd_o_b',
            'bio',
            'avatar',
            'background',
        ]
        widgets = {
            'First name',
                forms.CharField(),
            'Last name',
                forms.CharField(),
            'Email',
                forms.Textarea(attrs={
                'rows': 1,
            }),
            'Date_of_Birth',
                forms.DateField(),
            'Bio',
                forms.Textarea(attrs={
                'rows': 3,
            }),
            'Avatar',
                CloudinaryFileField(),
            'Background',
                CloudinaryFileField(),
        }
