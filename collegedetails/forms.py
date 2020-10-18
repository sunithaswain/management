from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registerform_model


class Signinform(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250)

class Registerform(forms.Form):
    username=forms.CharField(max_length=250,error_messages={'required': 'This field required!'})
    Email = forms.CharField(max_length=250,error_messages={'required': 'This field required!'})
    password = forms.RegexField(min_length=10,regex=r'^\+?1?\d{10}$',   error_messages = {'required':"Please enter valid mobile number."})
    #password = forms.CharField(max_length=250,error_messages={'required': 'This field required!'})
    Address=forms.CharField(max_length=250,error_messages={'required': 'This field required!'})
    Mobilenumber=forms.CharField(max_length=250,error_messages={'required': 'This field required!'})
    def clean_username(self):
            username = self.cleaned_data.get('username')
            email = self.cleaned_data.get('Email')
            if username and Registerform_model.objects.filter(name=username).exclude(email=email).count():
                raise forms.ValidationError("user already registerd")
                return username
    def clean(self):
            password =self.cleaned_data.get('password')
            #password2 =self.cleaned_data.get('password2')
            del self.cleaned_data['password']
            return password

class changeform(forms.Form):
    oldpassword=forms.CharField(max_length=250)
    newpassword = forms.CharField(max_length=250)


class Uploadform(forms.Form):
    image = forms.ImageField()
class contactform(forms.Form):
    user_name=forms.CharField(max_length=250)
    email=forms.CharField(max_length=250)
    projectdetails=forms.CharField(max_length=250)
class emailform(forms.Form):
    username=forms.CharField(max_length=250)
    password=forms.CharField(max_length=250)
