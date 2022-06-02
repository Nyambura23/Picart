from email.mime import image
from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    tag = models.CharField(max_length =30)

    def __str__(self):
        return self.tag
    
    def save_tag(self):
      self.save()

    def delete_tag(self):
      self.delete()

    class Meta:
      ordering = ['tag']

class Image(models.Model):
  image

