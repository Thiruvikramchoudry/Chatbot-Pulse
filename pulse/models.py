from django.db import models

# Create your models here.

class user_details(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username


class chat_message_100(models.Model):
    username=models.CharField(max_length=50)
    chat_type=models.CharField(max_length=50)
    message_type=models.CharField(max_length=50)
    img_url=models.FileField(default=None)
    message=models.CharField(max_length=1000)


    def __str__(self):
        return self.username


class chat_message_101(models.Model):
    username = models.CharField(max_length=50)
    chat_type = models.CharField(max_length=50)
    message_type = models.CharField(max_length=50)
    img_url = models.FileField(default=None)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.username


class chat_message_200(models.Model):
    username = models.CharField(max_length=50)
    chat_type = models.CharField(max_length=50)
    message_type = models.CharField(max_length=50)
    img_url = models.FileField(default=None)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.username