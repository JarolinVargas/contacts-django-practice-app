from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=255)
  email = models.EmailField(null=True)
  phone = models.CharField(max_length=15)

  # Add to admin dashboard
  def __str__(self):
    return f"{self.full_name}"