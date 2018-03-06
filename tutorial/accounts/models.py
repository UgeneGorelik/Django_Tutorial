from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import  post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='ashdod')

class UserProfile(models.Model):
    user =models.OneToOneField(User,on_delete='CASCADE')
    description = models.CharField(max_length=120,default='')
    city =models.CharField(max_length=120,default='')
    website=models.URLField(default='')
    phone =models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)
    ashdod=UserProfileManager()



def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile =UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)