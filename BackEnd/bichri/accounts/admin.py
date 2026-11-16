from django.contrib import admin
from .models import Rating, User
# Register your models here.
admin.site.register(User)
admin.site.register(Rating)