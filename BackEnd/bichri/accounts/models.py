from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=8, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=8, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_images/',blank=True,null=True)

    def __str__(self):
        return self.username


class Rating(models.Model):
    reviewer_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "ratings_given")
    seller_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "ratings_received")
    score = models.PositiveIntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)], default=0)
    comment = models.TextField(blank = True, null= True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Rating by {self.reviewer_id.username} for {self.seller_id.username}: {self.score} stars"

    