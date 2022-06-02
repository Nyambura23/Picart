from django.test import TestCase
from .models import User,tags


class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.miss= User(first_name = 'Miss', last_name ='Bdnk', email ='bdnk@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.miss,User))

        # Testing Save Method
    def test_save_method(self):
        self.miss.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)