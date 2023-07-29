"""
URL configuration for ChatPulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('chatbox',views.chatbox,name="chatbox"),
    path('send_message',views.send_message,name="send_message"),
    path('getmessages0',views.getmessages0,name="getmessages0"),
    path('getmessages1',views.getmessages1,name="getmessages1"),
    path('doctor_login',views.doctor_login,name="doctor_login"),
    path('getmessages2',views.getmessages2,name="getmessages2"),
    path('getmessages20',views.getmessages20,name="getmessages20"),
    path('send_message_docend',views.send_message_docend,name="send_message_docend"),
    path('close_session',views.close_session,name="close_session"),
]

