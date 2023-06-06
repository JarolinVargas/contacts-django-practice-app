from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper.form_method = "post"  # get or post
          self.helper.render_required_fields = True

        help_texts = {
          'username': '',
          'password1': '',
          'password2': '',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# jarolin, sodfijas82ks
class UserSignInForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)