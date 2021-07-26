from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=CASCADE)
  first_name = models.CharField(max_length=144)
  last_name = models.CharField(max_length=144)
  email = models.EmailField()
  profile_picture = CloudinaryField('image')

GENDER_CHOICES = (
  ("Male", "Male"),("Female","Female")
)

class Patient(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  id_number = models.IntegerField(blank=True)
  birth_certificate_no = models.IntegerField(blank=True)
  gender = models.CharField(max_length=15, choices= GENDER_CHOICES)
  age = models.IntegerField()

class Visit(models.Model):
  date_visited = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  note = models.TextField()
