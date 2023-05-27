from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper.form_method = "post"  # get or post
          self.helper.render_required_fields = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper.form_method = 'POST'  # get or post
          self.helper.render_required_fields = True

        def clean(self):
          cleaned_data = super().clean()  # Call the superclass's clean() method
          # Your custom validation logic here
          return cleaned_data