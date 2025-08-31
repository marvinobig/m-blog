from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'passwordConfirm']
    
    def clean(self):
        cleanedData = super().clean()
        password = cleanedData.get('password')
        passwordConfirm = cleanedData.get('passwordConfirm')

        if password and passwordConfirm and password != passwordConfirm:
            raise forms.ValidationError("Passwords do not match")