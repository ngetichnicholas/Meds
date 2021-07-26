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
