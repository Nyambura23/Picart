from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

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
    image = CloudinaryField('image')
    name =  models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags) 
    
    def __str__(self):
        """
    A method that returns an image through its name
     """
        return self.name
    
    def save_image(self):
        """
    A method that saves an image
     """
        self.save()
        
    def delete_image(self):
        """
    A method that delets an image
     """
        self.delete()    
    
    def get_image_by_id(id):
        """
    A method that gets an image by its id
     """
        image = Image.objects.get(id)
        return image
        
    @classmethod
    def all_images(cls):
        """
    A method that gets all images
     """
        images = cls.objects.all()
        return images    
    
    @classmethod
    def search_image(cls,search_term):
        """
    A method that searches an image
     """
        images = cls.objects.filter(tags__tag=search_term)
        return images

 
