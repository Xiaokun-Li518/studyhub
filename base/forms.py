from .models import *

from django.forms import ModelForm


from django.contrib.auth.forms import UserCreationForm




class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields ='__all__'
        exclude = ['host', 'participants']



class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']        
