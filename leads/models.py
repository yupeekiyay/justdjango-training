from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save

class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    country = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    

class Lead(models.Model):
    SOURCE_CHOICES = (
    ('YT','Youtube'),
    ('Google','Google'),
    ('Newsletter','Newsletter'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent",null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True,)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    #deal_calculator = models.OneToOneField("ProfitabilityCalculator", on_delete=models.PROTECT, null=True)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES,max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name

class ProfitabilityCalculator(models.Model):
    pass



class Category(models.Model):
    name = models.CharField(max_length=100) # New, Contacted, Converted, Unconverted
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_user_created_signal(sender,instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

