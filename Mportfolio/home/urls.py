from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="contact"),
    path('dashboard/', views.dashboard, name="contact"),
    path('dashboard/about', views.adminAbout, name="contact"),
    path('dashboard/home', views.dashboard, name="contact"),
    path('dashboard/portfolio', views.AdminPortfolio, name="contact"),
    path('dashboard/contact', views.Messages, name="contact"),
    path('uploadPic/', views.uploadPic, name='uploadPic'),
    path('dltPortfolio/<int:id>', views.dltPortfolio, name='dltPortfolio'),
    path('editPortfolio/<int:id>', views.editPortfolio, name='editPortfolio'),
    path('portPic/<int:id>', views.portPic, name='portPic'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handelLogout, name='logout'),
]
