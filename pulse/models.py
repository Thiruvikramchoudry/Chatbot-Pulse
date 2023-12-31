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
    message=models.CharField(max_length=100000)
    image = models.ImageField(null=True, upload_to="pulse/static/user_images")


    def __str__(self):
        return self.username


class chat_message_101(models.Model):
    username = models.CharField(max_length=50)
    chat_type = models.CharField(max_length=50)
    message_type = models.CharField(max_length=50)
    message = models.CharField(max_length=100000)
    image = models.ImageField(null=True, upload_to="pulse/static/user_images")
    def __str__(self):
        return self.username


class chat_message_200(models.Model):
    username = models.CharField(max_length=50)
    doctor_name=models.CharField(max_length=50)
    message=models.CharField(max_length=100000)
    message_type=models.CharField(max_length=50)
    chat_type=models.CharField(max_length=50)
    image=models.ImageField(null=True,upload_to="pulse/static/user_images")
    def __str__(self):
        return self.username

class doctor_detail(models.Model):
    username=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class client_request(models.Model):
    username=models.CharField(max_length=50)
    disease=models.CharField(max_length=50)
    def __str__(self):
        return self.username


class doner_details(models.Model):
    doner_name=models.CharField(max_length=50)
    mobile_number=models.IntegerField()
    doner_gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50)
    disease_status=models.CharField(max_length=10)
    def __str__(self):
        return self.doner_name