from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # extending the class
    # already has all the basic variables such as username, email and password
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional classes
    portfolio_site = models.URLField(blank=True) #user does not have to provide

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) #location to upload
                                                                         #media/profile_pics

    def __str__(self):
        return self.user.username
