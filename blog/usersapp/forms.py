from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser

class RegistrationForm(UserCreationForm):
    class Meta:
         model = BlogUser
         fields = ('usermname', 'password1', 'password2', 'email')
