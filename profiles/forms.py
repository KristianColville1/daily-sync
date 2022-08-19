from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Creates a form object for the profile model
    """

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'd_o_b',
            'avatar',
            'background',
        )
        widgets = {
            'First name'
        }
