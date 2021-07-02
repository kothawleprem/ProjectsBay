from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django .forms import ModelForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','phone','age','ctag','address','profession','organization','portfolio','github']
        widgets = {'name':forms.TextInput(),'phone':forms.TextInput(),'ctag':forms.TextInput(),'age':forms.TextInput(),'profession':forms.TextInput(),'organization':forms.TextInput(),'portfolio':forms.TextInput(),'address':forms.TextInput(),'github':forms.TextInput()}

class ClientAddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','tag','description','created','completed','achievements','tech','github','live','opf1','opfl1','opf2','opfl2','opf3','opfl3','opf4','opfl4','imgl']
        widgets = {'title':forms.TextInput(),'tag':forms.TextInput(),'description':forms.TextInput(),'created':forms.TextInput(),'completed':forms.TextInput(),'achievements':forms.Textarea(),'tech':forms.TextInput(),'github':forms.TextInput(),
        'live':forms.TextInput(),'opf1':forms.TextInput(),'opfl1':forms.TextInput(),'opf2':forms.TextInput(),'opfl2':forms.TextInput(),'opf3':forms.TextInput(),'opfl3':forms.TextInput(),'opf4':forms.TextInput(),'opfl4':forms.TextInput(),
        'imgl':forms.TextInput()}





