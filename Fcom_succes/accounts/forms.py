from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    occupation= forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','email','occupation','password1','password2']
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.occupation = self.cleaned_data["occupation"]
        if commit:
            user.save()
        return user
