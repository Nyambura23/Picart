from django.test import TestCase
from .models import User,Location, Image, tags


class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.miss= User(first_name = 'Miss', last_name ='Bdnk', email ='bdnk@gmail.com')
        self.miss.save_user()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.miss,User))

        # Testing Save Method
    def test_save_method(self):
        self.miss.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Bee= Image(id = '1', image = 'example.jpg', name = 'Bee', description ='Just one of my favourite photos', location ='Nairobi', tags ='Portrait')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Bee,Image)) 
    
     # Testing Save Method
    def test_save_method(self):
        self.Bee.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  

class LocationTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Nairobi= Location(location='Nairobi')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))    
        
    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)    
        
    def test_delete_method(self):
        self.Nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class tagsTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Portrait= tags(tag='Portrait')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Portrait,tags))    
        
    def test_save_method(self):
        self.Portrait.save_tag()
        tag = tags.objects.all()
        self.assertTrue(len(tag)>0)    
        
    def test_delete_method(self):
        self.Portrait.delete_tag()
        tag = tags.objects.all()
        self.assertTrue(len(tag)==0)
