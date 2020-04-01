from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxLengthValidator
from django.dispatch import receiver
from django.db.models.signals import post_save



class Department(models.Model):
    name = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name



class UserAdditionInfo(models.Model):
     user = models.OneToOneField(User, default=1,on_delete=models.CASCADE, related_query_name='userinfo')
     department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()





