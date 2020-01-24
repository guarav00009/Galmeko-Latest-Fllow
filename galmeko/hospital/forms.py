from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from hospital.models import Hospital


class CustomHospitalCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Hospital
        fields = ('hospital_name','registration_no',)

