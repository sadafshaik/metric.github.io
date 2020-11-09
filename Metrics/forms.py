
from django import forms
from django.core import validators

from Metrics.models import user


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only stringss are allowed")



class userForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.mail

    class Meta:
        model=user
        fields=['name','passwd','cwpasswd','mail','mobileno','qualification','status']
    def clean(self):
        cleaned_data=super().clean()
        inputpasswd=cleaned_data['passwd']
        inputcwpasswd=cleaned_data['cwpasswd']
        if inputpasswd!=inputcwpasswd:
            raise forms.ValidationError("password should match")









