# Import necessary modules from Django and setup URL patterns
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chat.urls'))
]
