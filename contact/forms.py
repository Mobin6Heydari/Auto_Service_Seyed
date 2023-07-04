from django import forms
from django.core import validators


class UserContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}), validators=[validators.EmailValidator])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), validators=[validators.MaxLengthValidator(11)])
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

