from django import forms
from django.contrib.auth.models import User
from Registration.models import Registration_Info





class RegistrationForm(forms.ModelForm):
    College_Name = forms.CharField(widget=forms.TextInput(attrs={'style':'color:black;width:500px'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'style':'color:black;width:500px'}))
    Number_of_Participants = forms.IntegerField(widget=forms.TextInput(attrs={'style':'color:black;width:500px'}))
    Email =forms.CharField(widget=forms.TextInput(attrs={'style':'color:black;width:500px;'}))
    Contact = forms.CharField(widget=forms.TextInput(attrs={'style':'color:black;width:500px'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'style':'color:black;width:500px', }))

    class Meta :
        model = Registration_Info

        fields = (
                    'College_Name', 'Number_of_Participants', 'Contact', 'Email', 'Address'

        )
