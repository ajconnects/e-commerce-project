from django import forms
from .models import ProgrammerProfile, ClientProfile

class ProgrammerProfileForm(forms.ModelForm):
    class Meta:
        model = ProgrammerProfile
        fields = '__all__'

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = '__all__'