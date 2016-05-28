from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bot.models import UserProfile


class UserProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'has_accepted_terms_and_conditions',
        )
        widgets = {
            'has_accepted_terms_and_conditions': forms.CheckboxInput(attrs={'class': "uniform", }),
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type': "password", 'class': "form-control", }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type': "password", 'class': "form-control", }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", }))

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'A User is already using this email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
