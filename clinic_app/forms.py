from django import forms
from django.db.models import fields
from .models import *

class AddPatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ('first_name','last_name','id_name','birth_certificate_no','gender','age','phone')