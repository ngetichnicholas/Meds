from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class ClinicalStaff(models.Model):
  staff = models.OneToOneField(User,on_delete=CASCADE)
  first_name = models.CharField(max_length=144)
  last_name = models.CharField(max_length=144)
  email = models.EmailField()
  profile_picture = CloudinaryField('image')

  def __str__(self):
    return self.user.username

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

class Visit(models.Model):
  date_visited = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  patient = models.ForeignKey(Patient,on_delete=CASCADE)
  note = models.TextField()
