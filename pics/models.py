from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=60)
    
    def __str__(self):
        """
    A method that returns a location as a string
     """
        return self.location 
    
    def save_location(self):
        """
    A method that saves a location
     """
        self.save()
    
    def delete_location(self):
        """
    A method that deletes a location
     """
        self.delete()
    
    class Meta:
        ordering = ['location']


class categories(models.Model):
    category = models.CharField(max_length=60)
     
    def __str__(self):
        """
    A method that returns a category as a string
     """
        return self.category    
    
    def save_category(self):
    
        self.save()
    
    def delete_category(self):

        self.delete()
    
    class Meta:
        ordering = ['category']   


class Image(models.Model):
    image = CloudinaryField('image')
    name =  models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(categories , null=True) 
    
    def __str__(self):
    
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
        images = cls.objects.filter(categories__category=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        """
    A method that filters images using a location
     """
        image_location = cls.objects.filter(location__location=location).all()
        return image_location       
