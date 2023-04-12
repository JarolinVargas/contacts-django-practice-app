from django.db import models

# Create your models here.
class Contact(models.Model):
  full_name = models.CharField(max_length=255)
  email = models.EmailField(null=True)
  phone = models.CharField(max_length=15)

  # Add to admin dashboard
  def __str__(self):
    return f"{self.full_name}"