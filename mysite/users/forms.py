from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    class Meta:
        model= User
        fields= ["username","first_name","last_name","email","password1","password2"]

    def __init__(self,*args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'w-full px-3 py-2 border border-gray-300 rounded'
            })

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ["username","email"]
        exclude= ["password1","password2"]