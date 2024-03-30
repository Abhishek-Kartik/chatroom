
# Import necessary modules and views from Django
from django.urls import path
from .import views


# Define URL patterns for the application
urlpatterns = [
  #URL to the home view function
  path('',views.home, name= 'home'),
  
  # URL with room to the room view function
  path('<str:room>/', views.room, name='room'),

  #'checkview' URL to the checkview view function
  path('checkview',views.checkview, name='checkview'),

  path('send', views.send, name='send'),

  path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]