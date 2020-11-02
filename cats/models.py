from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Color(models.Model):
    color_name = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.color_name}"
   
class Cat(models.Model):
    cat_name = models.CharField(max_length=20)
    color_id = models.ForeignKey(Color, null=True, blank=True, related_name="Color", on_delete=models.SET_NULL)
    gender = models.BooleanField()
    owner =  models.ForeignKey(User, null=True, blank=True, related_name="Cat_owner", on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.cat_name}"
    
class Prey(models.Model):
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.type}"
    
class Hunting(models.Model):
    cat_id = models.ForeignKey(Cat, null=True, blank=True, related_name="Cat", on_delete=models.SET_NULL)
    prey_id = models.ForeignKey(Prey, null=True, blank=True, related_name="Prey", on_delete=models.SET_NULL)
    duration = models.DurationField()
    cat_owner =  models.ForeignKey(User, null=True, blank=True, related_name="Cat_hunting_owner", on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.id}"
      
class Usr(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    cat1_id = models.ForeignKey(Cat, null=True, blank=True, related_name="Cat1", on_delete=models.SET_NULL)
    cat2_id = models.ForeignKey(Cat, null=True, blank=True, related_name="Cat2", on_delete=models.SET_NULL)
    cat3_id = models.ForeignKey(Cat, null=True, blank=True, related_name="Cat3", on_delete=models.SET_NULL)
    cat4_id = models.ForeignKey(Cat, null=True, blank=True, related_name="Cat4", on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.user_name}"