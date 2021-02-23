from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
 

class CustomUser(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    

class Lead(models.Model):
    SOURCE_CHOICES = (
    ('YT','Youtube'),
    ('Google','Google'),
    ('Newsletter','Newsletter'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.PROTECT)
    #deal_calculator = models.OneToOneField("ProfitabilityCalculator", on_delete=models.PROTECT, null=True)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES,max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name

class ProfitabilityCalculator(models.Model):
    pass
