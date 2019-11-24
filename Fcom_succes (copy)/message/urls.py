from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main, name='message.main'),
    path('result/', views.result, name='message.result'),
    path('sent/', views.sent_messages, name='message.sent'),
]
