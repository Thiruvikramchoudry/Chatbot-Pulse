from django.contrib import admin
from .models import user_details,chat_message_100,chat_message_101,chat_message_200,client_request,doctor_detail
# Register your models here.


admin.site.register(user_details)
admin.site.register(chat_message_100)
admin.site.register(chat_message_101)
admin.site.register(chat_message_200)
admin.site.register(client_request)
admin.site.register(doctor_detail)

