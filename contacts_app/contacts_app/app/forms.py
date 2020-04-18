from django import forms
from django.contrib.auth.models import User
from app.models import UserProfileInfo,ContactsInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password',)

class ContactsInfoForm(forms.ModelForm):
	class Meta():
		model =  ContactsInfo
		fields = ('name','contact_entry',)


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('contact_number',)