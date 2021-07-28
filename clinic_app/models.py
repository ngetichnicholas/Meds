from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
from django.db.models.fields import DateTimeField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class ClinicalStaff(models.Model):
  staff = models.OneToOneField(User,on_delete=CASCADE)
  first_name = models.CharField(max_length=144)
  last_name = models.CharField(max_length=144)
  email = models.EmailField()
  profile_picture = CloudinaryField('image')

  def __str__(self):
    return self.staff.username

@receiver(post_save, sender=User)
def update_staff_signal(sender, instance, created, **kwargs):
  if created:
      ClinicalStaff.objects.create(staff=instance)
  instance.clinicalstaff.save()

GENDER_CHOICES = (
  ("Male", "Male"),("Female","Female")
)

class Patient(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  id_number = models.IntegerField(blank=True,null=True)
  birth_certificate_no = models.IntegerField(blank=True,null=True)
  gender = models.CharField(max_length=15, choices= GENDER_CHOICES)
  age = models.IntegerField()
  phone = models.IntegerField(blank=True,null=True)

  def save_patient(self):
    self.save()

  def delete_patient(self):
    self.delete()

  def __str__(self):
    return self.first_name

class Visit(models.Model):
  date_visited = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  note = models.TextField()

  def save_visit(self):
    self.save()

  def delete_visit(self):
    self.delete()

  def __str__(self):
      return self.patient.first_name

class Medicine(models.Model):
  name = models.CharField(max_length=144)

  def save_medicine(self):
    self.save()

  def delete_medicine(self):
    self.delete()

  def __str__(self):
    return self.name

class Prescription(models.Model):
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  drug = models.ForeignKey(Medicine,on_delete=CASCADE)
  prescriber = models.ForeignKey(ClinicalStaff,on_delete=CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  note = models.TextField()

  def save_prescription(self):
    self.save()

  def delete_prescription(self):
    self.delete()

  def __str__(self):
    return self.patient.first_name

class PatientHealthHistory(models.Model):
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  date_recorded = models.DateTimeField(auto_now_add=True)
  health_record = models.TextField()

  def save_patient_health_history(self):
    self.save()

  def delete_patient_health_history(self):
    self.delete()

  def __str__(self):
    return self.patient.first_name

class PatientAppointment(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  gender = models.CharField(max_length=15, choices= GENDER_CHOICES)
  age = models.IntegerField()
  phone = models.IntegerField(blank=True,null=True)
  date_made = models.DateTimeField(auto_now_add=True)
  appointment_date = DateTimeField(default=timezone.now)

  def save_patient_appointment(self):
    self.save()

  def delete_patient_appointment(self):
    self.delete()

  def __str__(self):
    return self.first_name

class FeedBack(models.Model):
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  feedback_message = models.TextField()
  feedback_date = models.DateTimeField(auto_now_add=True)

  def save_feedback(self):
    self.save()

  def delete_feedback(self):
    self.delete()

  def __str__(self):
    return self.patient.first_name

