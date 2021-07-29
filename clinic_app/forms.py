from django import forms
from django.db.models import fields
from .models import *

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ('first_name','last_name','id_number','birth_certificate_no','gender','age','phone')

class AppointmentForm(forms.ModelForm):
  class Meta:
    model = PatientAppointment
    fields = ('first_name','last_name','gender','age','phone','appointment_date','approve')

class PrescriptionForm(forms.ModelForm):
  class Meta:
    model = Prescription
    fields = ('patient','dose','drug','prescriber','note')

class DrugForm(forms.ModelForm):
  class Meta:
    model = Medicine
    fields = ('name','description')

class HealthHistoryForm(forms.ModelForm):
  class Meta:
    model = PatientHealthHistory
    fields = ('patient','health_record')

class FeedbackForm(forms.ModelForm):
  class Meta:
    model = FeedBack
    fields = ('patient','feedback_message')

class VisitForm(forms.ModelForm):
  class Meta:
    model = Visit
    fields = ('patient','note')