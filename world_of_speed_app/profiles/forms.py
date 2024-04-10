from django import forms

from world_of_speed_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', )


        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture', )




