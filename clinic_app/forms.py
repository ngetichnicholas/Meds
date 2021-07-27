from django import forms
from django.db.models import fields
from .models import *

class AddPatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ('first_name','last_name','id_number','birth_certificate_no','gender','age','phone')

class AddAppointmentForm(forms.ModelForm):
  class Meta:
    model = PatientAppointment
    fields = ('first_name','last_name','gender','age','phone','appointment_date')

class AddPrescriptionForm(forms.ModelForm):
  class Meta:
    model = Prescription
    fields = ('patient','drug','prescriber','note')