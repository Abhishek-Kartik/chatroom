from django.contrib import admin
from .models import Room, Message


# Register your models here.

# Register models with the admin interface

# Register the Room model with the admin interface
admin.site.register(Room)

# Register the Message model with the admin interface
admin.site.register(Message)