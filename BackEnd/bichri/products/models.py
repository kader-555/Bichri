from django.db import models
from accounts.models import User 


class Product(models.Model):
    # image= models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    description = models.CharField( max_length=500)
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now = True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(unique = True, max_length=200)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    position = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Image for {self.product.title}"

    