from django.shortcuts import render,redirect

from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from .models import  user_details,chat_message_100,chat_message_101,chat_message_200
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pulse.image_validation import validate_image
from pulse.disease_classifier import check_disease
from pulse.cancer_classifier import check_cancer
from pulse.benign_malignant import spread_prediction





# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return render(request,'pulse/index.html')
    elif(request.user.is_superuser):
        auth.logout(request)
        return redirect('/')
    else:
        username=request.user
        return render(request, 'pulse/main.html',{'username':username})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if len(user_details.objects.filter(username=username,password=password))==1:
                auth.login(request, user)
        return redirect('/')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user=user_details(username=username,password=password)
        new_user.save()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        user_access=authenticate(username=username,password=password)
        auth.login(request,user)
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def chatbox(request):

    return render(request,'pulse/chatarea.html',{'username':request.user})


def send_message(request):

    if request.method == 'POST':
        try:
            image = request.FILES["image"]
        except:
            image=None
        message=request.POST["message"]
        chatbox_type=str(request.POST["chatbox_type"])


        if image:
            message_type="message_image"
        else:
            message_type="message"


        if chatbox_type=="0":
            new_message=chat_message_100(username=request.user,image=image,message_type=message_type,message=message,chat_type="user")
        elif chatbox_type=="1":
            new_message=chat_message_101(username=request.user,image=image,message_type=message_type,message=message,chat_type="user")
        else:
            new_message=chat_message_200(username=request.user,image=image,message_type=message_type,message=message,chat_type="user")
        new_message.save()


        if image:
            if chatbox_type=="1":
                skin_percentage=validate_image(image)
                if skin_percentage<70:
                    chat_message=chat_message_101(username=request.user,image=image,message_type=message_type,message="Invalid Image",chat_type="bot")
                    chat_message.save()
                else:
                    chat_message = chat_message_101(username=request.user, image=image, message_type=message_type,message="Valid Image", chat_type="bot")
                    chat_message.save()
                    disease_type=check_disease(image)
            elif chatbox_type=="0":

                skin_percentage=validate_image(image)
                if skin_percentage<80:
                    chat_message=chat_message_100(username=request.user,image=image,message_type=message_type,message="Invalid Image",chat_type="bot")
                    chat_message.save()

                else:
                    chat_message=chat_message_100(username=request.user,image=image,message_type=message_type,message="Valid Image",chat_type="bot")
                    cancer_type=check_cancer(image)
                    print(cancer_type)
                    cancer_response=chat_message_100(username=request.user,image=image,message_type=message_type,message="Based on the Image ,it looks like "+cancer_type,chat_type="bot")
                    cancer_spread_type=spread_prediction(image)
                    cancer_spread_type_response="It look like a "+cancer_spread_type
                    if cancer_spread_type=="malignant":
                        cancer_spread_type_response+= " which means it can be spreadable and cause death if it's not taken any consern"
                    else:
                        cancer_spread_type_response+= " which means it seem's to be not spreadable and doesn't cause any death"
                    cancer_spread=chat_message_100(username=request.user,image=image,message_type=message_type,message=cancer_spread_type_response,chat_type="bot")

                    chat_message.save()
                    cancer_response.save()
                    cancer_spread.save()






        return JsonResponse({'message': 'Data saved successfully'})  # Return a JSON response


def getmessages0(request):
    chat_message=chat_message_100.objects.filter(username=request.user)
    text=[]
    for message in chat_message:

        if message.image!="":
            img=(message.image.name).split("/")
            img=img[-2]+'/'+img[-1]
        else:
            img=None
        text.append([message.message,img,message.chat_type])

    return JsonResponse({"messages": text})

def getmessages1(request):
    chat_message=chat_message_101.objects.filter(username=request.user)
    text=[]
    for message in chat_message:

        if message.image!="":
            img=(message.image.name).split("/")
            img=img[-2]+'/'+img[-1]
        else:
            img=None
        text.append([message.message,img,message.chat_type])

    return JsonResponse({"messages": text})



