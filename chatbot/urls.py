from django.urls import path

from chatbot import views

urlpatterns = [
    path('chat/', views.chatbot, name='chatbot'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]