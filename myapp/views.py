from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# import pandas as pd
from twilio.rest import Client
from .forms import TemporaryUserForm
import smtplib
from django.contrib.auth import authenticate , login as userlogin ,logout
from django.http import response
from requests.api import request
# from myapp.models import userimages
# from myapp.models import ssidPassword
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
# from .models import employees
# from .serializers import employeesSerializer
from django.shortcuts import get_object_or_404
# from myapp.models import Videos
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,password_validation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm, SubUserRegisterForm, PasswordChangeForm, PasswordChangingForm, ImageForm,TemporaryUserForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, context
from myapp.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
# from myapp.serializers import testimageSerializers,userSerializers,placeSerializers,floorSerializers,flatSerializers,roomSerializers,deviceSerializers,pinscheduleSerializers,pinscheduleTimeSerializers,deviceStatusSerializers,emernumberSerializers,sensorSerializers,ssidPasswordSerializers,pinnamesSerializers,userprofileimagesSerializers,deviceipaddressSerializers,subuseraccessSerializers,emailSerializers,subuseremailSerializers,subuserplaceSerializers,subuserplacegetSerializers,tempuserregisterSerializers,placenameSerializers,floornameSerializers,roomnameSerializers,otpfortampuserSerializers,otpuserloginSerializers,firstnameSerializers,flatSerializers,userlogingetdataSerializers,flatnameSerializers,dateasignSerializers,timeasignSerializers, energySerializers, onehourenSerializers
from myapp.serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import serializers
from rest_framework import status
import random, math
from datetime import date
import json
import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
import http.client
import ast
# from twilio.rest import Client
from myapp import utils
from myapp.utils import get_variable
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
import time
from datetime import datetime
from datetime import date
# from background_task import background
from rest_framework.generics import ListCreateAPIView
import pandas as pd
import uuid
conn = http.client.HTTPConnection("2factor.in")

# Create your views here.
# class Exlfiledownload(APIView):
#     def  get(self,request):
#         exl_obj = exl_files.objects.all()
#         exl_serial = exlSerializers(exl_obj, many=True  )
#         df = pd.DataFrame(exl_serial.data)
#         df.to_csv(f"staticfile/{uuid.uuid4()}.csv" , encoding="UTF-8" ,index=False)
#         print(df)
#         return Response({"status":200,})
@api_view(["GET","POST","PUT"])
def Exlfile(request):
    if request.method == "GET":
        exl_obj = exl_files.objects.all()
        exl_serial = exlSerializers(exl_obj, many=True  )
        df = pd.DataFrame(exl_serial.data)
        df.to_csv(f"staticfile/{uuid.uuid4()}.csv" , encoding="UTF-8" ,index=False)
        return Response({"status":200,})

@api_view(["GET","POST","PUT"])
def ssidList(request):
    if request.method == "GET":
        device_data = ssidPassword.objects.filter(d_id=request.GET['d_id'])
        roomJson = ssidPasswordSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = ssidPasswordSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        try:
            device_object=ssidPassword.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ssidPasswordSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ##
@api_view(["GET","POST","PUT"])
def emerNumber(request):
    if request.method=="GET":
        enumdata = emergencyNumber.objects.filter(user = request.user,d_id=request.GET['d_id'])
        emernumberJson = emernumberSerializers(enumdata, many=True)
        dd = emernumberJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = emernumberSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
####
    elif request.method =="PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        try:
            device_object=emergencyNumber.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = emernumberSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def tempuserautodelete():
        now = datetime.today()
        now1=str(now)
        now2 = now1[:16:]
        dat1 = datetime.strptime(now2, "%Y-%m-%d  %H:%M")
        data1 = tempuser.objects.all()
        pinscheduledlist = pinschedule.objects.all()
        dataJson = dateasignSerializers(data1, many=True)
        pinjson = pinscheduleSerializers(pinscheduledlist,many=True)
        
        for data in dataJson.data:
            _date = data['date']
            _timing = data['timing']
            _id = data['id']
            dateTimeVal = _date+" "+_timing
            tempdate = datetime.strptime(dateTimeVal, "%Y-%m-%d  %H:%M")
            if(tempdate <=  dat1):
              data2 = tempuser.objects.filter(id=_id)
              data2.delete() 
              print(_id)
              print("delete")
            else:
                print("NOOOOOOOOOOOOOOOOOOO")
            
        
        for pinData in pinjson.data:
            _date = pinData['date']
            _timing = pinData['timing']
            _id = pinData['id']
            dateTimeVal = _date+" "+_timing
            pindate = datetime.strptime(dateTimeVal, "%Y-%m-%d  %H:%M")
            if(pindate <=  dat1):
              pinscheduleData = pinschedule.objects.filter(id=_id)
              deviceStatusObj =  deviceStatus.objects.get(pk=pinscheduleData[0].d_id)
              deviceStatusObj.d_id = pinscheduleData[0].d_id
              if(pinscheduleData[0].pin1Status is not None):
                deviceStatusObj.pin1Status = pinscheduleData[0].pin1Status

              if(pinscheduleData[0].pin2Status is not  None):
                deviceStatusObj.pin2Status = pinscheduleData[0].pin2Status

              if(pinscheduleData[0].pin3Status is not None):
                deviceStatusObj.pin3Status = pinscheduleData[0].pin3Status

              if(pinscheduleData[0].pin4Status is not  None):
                deviceStatusObj.pin4Status = pinscheduleData[0].pin4Status
              if(pinscheduleData[0].pin5Status is not  None):
                deviceStatusObj.pin5Status = pinscheduleData[0].pin5Status

              if(pinscheduleData[0].pin6Status is not None):
                deviceStatusObj.pin6Status = pinscheduleData[0].pin6Status

              if(pinscheduleData[0].pin7Status is not None):
                deviceStatusObj.pin7Status = pinscheduleData[0].pin7Status

              if(pinscheduleData[0].pin8Status is not None):
                deviceStatusObj.pin8Status = pinscheduleData[0].pin8Status

              if(pinscheduleData[0].pin9Status is not None):
                deviceStatusObj.pin9Status = pinscheduleData[0].pin9Status

              if(pinscheduleData[0].pin10Status is not None):
                deviceStatusObj.pin10Status = pinscheduleData[0].pin10Status
        
              if(pinscheduleData[0].pin11Status is not None):
                deviceStatusObj.pin11Status = pinscheduleData[0].pin11Status

              if(pinscheduleData[0].pin12Status is not None):
                deviceStatusObj.pin12Status = pinscheduleData[0].pin12Status
             
              deviceStatusObj.save()
              pinscheduleData.delete() 
            else:
                print("No Update")
            
        
        
def phonenumber(request):
    if request.method=="GET":
        data = phone.objects.filter(user=request.user)
        placeJson = phone_Serializers(data, many=True)
        print(data)
        return Response(placeJson.data)
        # dd = placeJson.data[:]
        # return Response(dd[0])
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = phone_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Post Data", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
def index(request):
    return HttpResponse("Hello pk ......")
class alldevice(ListCreateAPIView):
    queryset = allDevices.objects.all()
    serializer_class = allDeviceSerializers
  

@api_view(["GET","POST","PUT"])
def userdataList(request):
    if request.method=="GET":
        device_data = User.objects.filter(id=request.GET['id'])
        nameJson = userlogingetdataSerializers(device_data, many=True)
        # return Response(nameJson.data)
        dd = list(nameJson.data)[0]
        print(dd)
        return Response(dd)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def useridList(request):
    if request.method=="GET":
        current_user = request.user
        print(current_user.id)
        return Response(current_user.id)


                        ############################# hardware apis ############################### 


                                        ###########   Add   place   #################


                                        
@api_view(["GET","POST","PUT","DELETE"])
# @permission_classes([IsAuthenticated])
def placeList(request):
    if request.method=="GET":
        data = place.objects.filter(user=request.user)
        placeJson = placeSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
        # dd = placeJson.data[:]
        # return Response(dd[0])
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = placeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_variable(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['p_id']
        try:
            device_object=place.objects.get(p_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = placeSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = place.objects.filter(p_id=request.GET['p_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def placegetList(request):
    if request.method=="GET":
        data = place.objects.filter(user = request.user)
        placeJson = placeSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

#            ################### Without security ###################################

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def placegetallList(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(email=request.GET['email'])
        placeJson = subuserplacegetSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)



# ################ for subuser  #####################



#                                 ###########   Add   floor   #################


@api_view(["GET", "POST","PUT","DELETE"])
def fieldList(request):
    if request.method=="GET":
        floor_data = field.objects.filter(user = request.user,p_id=request.GET['p_id'])
        floorJson = fieldSerializers(floor_data, many=True)
        # dd = floorJson.data[:]
        return Response(floorJson.data)

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = fieldSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_variable(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['f_id']
        try:
            device_object=field.objects.get(f_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = fieldSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = field.objects.filter(f_id=request.GET['f_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
def fieldgetList(request):
    if request.method=="GET":
        floor_data = field.objects.filter(user = request.user,p_id=request.GET['p_id'])
        floorJson = fieldSerializers(floor_data, many=True)
        return Response(floorJson.data)

@api_view(["GET","POST"])
def fieldnamelist(request):
    if request.method == "GET":
        device_data = field.objects.filter(f_id=request.GET['f_id'])
        nameJson = fieldnameSerializers(device_data, many=True)
        # return Response(nameJson.data)
        # dd = list(nameJson.data)[0]["f_name"]
        # print(dd)
        return Response(nameJson.data)
#                 ################### Without security ###################################

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def fieldgetallList(request):
    if request.method=="GET":
        data = field.objects.filter(p_id=request.GET['p_id'])
        placeJson = fieldSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
#
#                                 ###########   Add Device      ################



@api_view(["GET","POST","DELETE"])
def deviceList(request):
    if request.method=="GET":
        room_data = device.objects.filter(user = request.user,f_id=request.GET['f_id'])
        roomJson = deviceSerializers(room_data, many=True)
        # rr = roomJson.data[:]
        return Response(roomJson.data)
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = deviceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = device.objects.filter(r_id=request.GET['f_id'], d_id=request.GET['f_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
def devicegetList(request):
    if request.method=="GET":
        room_data = device.objects.filter(user = request.user,f_id=request.GET['f_id'])
        devJson = deviceSerializers(room_data, many=True)
        return Response(devJson.data)


#                 ################### Without security ###################################

@api_view(["GET"])
def devicegetallList(request):
    if request.method=="GET":
        room_data = device.objects.filter(f_id=request.GET['f_id'])
        devJson = deviceSerializers(room_data, many=True)
        return Response(devJson.data)

#                                 ###########   Add   sensors   #################




#                                 ###########   PinStatus   #################
@api_view(["GET","POST","PUT"])
def devicePinStatus(request):

    if request.method == "GET":
        device_data = deviceStatus.objects.filter(d_id=request.GET['d_id'])
        roomJson = deviceStatusSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])


    elif request.method == "POST":
        received_json_data=json.loads(request.body)
       
        # if received_json_data['put']!='yes':
        serializer = deviceStatusSerializers(data=request.data)
        print(received_json_data)
       
        serializer = deviceStatusSerializers(data=request.data)
        # external_api_url = 'https://example.com/api/endpoint/'
        # data = request.POST
        # res = requests.post(external_api_url, data)

        if serializer.is_valid():
            serializer.save()
        # return Response(res.json())
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        print('all set')
        x1 = received_json_data['sensor1']
        x2 = received_json_data['sensor2']
        x3 = received_json_data['sensor3']
        x4 = received_json_data['sensor4']
        x5 = received_json_data['sensor5']
        x6 = received_json_data['sensor6']
        x7 = received_json_data['sensor7']
        x8 = received_json_data['sensor8']
        x9 = received_json_data['sensor9']
        x10 = received_json_data['sensor10']

        print("AEnoss ",x1)
        if x1 > 5:
            getAlldata(device_id)
          
        if x2 > 5: 
            getAlldata(device_id)
        if x3 > 5:
            getAlldata(device_id)
        if x4 > 5:
            getAlldata(device_id)
        if x5 > 5:
            getAlldata(device_id)
        if x6 > 5:
            getAlldata(device_id)
        if x7 > 5:
            getAlldata(device_id)
        if x8 > 5:
            getAlldata(device_id)
        if x9 > 5:
            getAlldata(device_id)
        if x10 > 5:
            getAlldata(device_id)

        try:
            print('excecuted')
            device_object=deviceStatus.objects.get(d_id=device_id)
            
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = deviceStatusSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_fcm_message(x,fcmToken):
    urls_api ="https://fcm.googleapis.com/fcm/send"
    server_key ="key=AAAAUOxNlRo:APA91bFeXi6tYaX5dP4OKKQHFfNK62CCbg36p59jp1VUHOQL9GDiyY8pGLmDqJ6XWq4dcVzr03OcgKevyY--gSqMHmK48tvlDulp69m_ATAa4IoHSV_YRwd91uDPlDIGfbwAlAUhu3b"
        
    fcm_message={"to":fcmToken,
                "notification":{
                "body":"Sensor "+str(x)+ " is High",
                "title":"200",
                "subtitle":"200" }
                 }
   
    headersdata = {
            'Authorization': "key=AAAAUOxNlRo:APA91bFeXi6tYaX5dP4OKKQHFfNK62CCbg36p59jp1VUHOQL9GDiyY8pGLmDqJ6XWq4dcVzr03OcgKevyY--gSqMHmK48tvlDulp69m_ATAa4IoHSV_YRwd91uDPlDIGfbwAlAUhu3bk",
            'Content-Type': 'application/json; UTF-8',
        }

    print('Message sent',headersdata)
  # [END use_access_token]
    resp = requests.post(urls_api, data=json.dumps(fcm_message), headers=headersdata)
    # resp=""
    print(resp.status_code)
    if resp.status_code == 200:
            print('Message sent to Firebase for delivery, response:')
            print(resp.text)
    else:
            print('Unable to send message to Firebase')
            print(resp.text)
### new
@api_view(["POST"])
def fire(request):
    received_json_data=json.loads(request.body)
    print(received_json_data)
        # if received_json_data['put']!='yes':
    serializer = FirebaseSer (data=request.data)
        

    if serializer.is_valid():
        serializer.save()
        # return Response(res.json())
        return Response("data created", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #    return response




def getAlldata(dId):
    getUser = device.objects.get(d_id=dId)
    print(getUser.user)
    getUsernFirebasetable(getUser.user)


def getUsernFirebasetable(userData):
    getUser = FirebaseDetails.objects.get(user=userData)
    print(getUser.fcm)

    send_fcm_message(1,getUser.fcm)   
### edit devicenabe
@api_view(["GET","POST","PUT"])
def devicePinNames(request):
    if request.method == "GET":
        device_data = deviceStatus.objects.filter(d_id=request.GET['d_id'])
        roomJson = deviceStatusSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = deviceStatusSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        print('all set')
        try:
            print('excecuted')
            device_object=deviceStatus.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = deviceStatusSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ################################### Update Pin Status For DilogFlow ###################################  OK GOOGLE  ######################

@api_view(["POST"])
def webhook(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        
        
        # action = req.get("queryResult").get("action")
        # d_id = req.get('queryresult').get('action')
        parameters = req.get("queryResult").get("parameters")
        # roomJson = deviceStatusSerializers(parameters, many=True)
        # device_id=req.get('queryresult').get('action')
        serializer = deviceStatusSerializers(data=parameters)
        # device_id=received_json_data['d_id']
        #     print('123')
        device_id=parameters['d_id']
        try:
            print('qwe')
            device_object=deviceStatus.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = deviceStatusSerializers(device_object, data=parameters)
        # serializer = deviceStatusSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



################ for subuser  #####################



                                ###########   Add   floor   #################



@api_view(["GET","POST","PUT","DELETE"])
def subuaccess(request):
    # if request.method=="GET":
    #     data = subuseraccess.objects.filter(user=request.user, p_id=request.GET['p_id'])
    #     placeJson = floorSerializers(data, many=True)
    #     print(data)
    #     return Response(placeJson.data)
    #     # return Response(device_data)

    if request.method == "POST":
        # received_json_data=json.loads(request.body)
        serializer = subuseraccessSerializers(data=request.data)
        # email12 = subuseraccess.objects.filter()
        # subJson1 = subuseremailSerializers(email12, many=True)
        # # success = False
        # for x in list(subJson1.data):
        #     xc = x["emailtest"]
        #     print(xc)
        # xc = ["emailtest"]
        # if User.objects.filter(email=xc).exists():
        #     print("ssucessss")
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response("data created", status=status.HTTP_201_CREATED)
        # email1 = subuseraccess.objects.filter(user=request.GET['user'])
        # email1 = "ppp@gm.com"
        # if User.objects.filter(email=email1).exists():
        # email = User.objects.filter(user=request.GET['email'])
        # if User.objects.get(user=request.GET['email']).exists():
        if serializer.is_valid():
            print("xtz")
            # email1 = "ppp@gm.com"
            # if User.objects.filter(email=email1).exists():
        # email1 = User.objects.get(user=request.GET['email'])
        # print(email1)
        # email1 = "pankajpalariya21@gmai.com"
        # email1 = request.POST['email']
            serializer.save()
            # email = subuseraccess.objects.filter(user=request.GET['email'])
            # print(email)
            email12 = subuseraccess.objects.filter()
            subJson1 = subuseremailSerializers(email12, many=True)
            success = False
            # for x in list(subJson1.data):
            xc = list(subJson1.data)[-1]["emailtest"]
            print(xc)
                # print(email12)
                # print(subJson1.data)
            if User.objects.filter(email=xc).exists():
                # user1 = User.objects.filter(name__contains='email')
                # user1 = User.objects.all()
                # print(user1)
                # userJson = userSerializers(user1, many=True)
                # main = list(userJson.data)
                # print(main)
                    # print(subuseraccess.emailtest)
                    # print(email)
                success = Response("email added as a SUB-USER", status=status.HTTP_201_CREATED)
            else:
                xcdelete = subuseraccess.objects.last()
                print(xcdelete)
                xcdelete.delete()
                return Response("Email not exists.")
            return success if success else Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = subuserplace.objects.filter(email=request.GET['email'], p_id=request.GET['p_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

########## for main user to get the list of subuser  ##############
@api_view(["GET"])
def subuplaceget(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(user=request.user)
        placeJson = subuserplacegetSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

# @api_view(["GET"])
# def subuserfind(request):
#     if request.method=="GET":
#         data = subuserplace.objects.filter(user=request.user)
#         dataJson = subuserplaceSerializers(data, many=True)
#         return Response(dataJson.data)

# @api_view(["GET"])
# def subuserfindsubuser(request):
#     if request.method=="GET":
#         data = subuserplace.objects.filter(email=request.GET['email'])
#         dataJson = subuserplaceSerializers(data, many=True)
#         return Response(dataJson.data)

@api_view(["GET","POST","PUT"])
def subuplace(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(email=request.GET['email'])
        placeJson = subuserplacegetSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
        # return Response(device_data)

    elif request.method == "POST":
        # received_json_data=json.loads(request.body)
        serializer = subuserplaceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email1 = subuserplace.objects.filter()
            subJson1 = subuserplaceSerializers(email1, many=True)
            xc = list(subJson1.data)[-1]["p_id"]
            xc1 = list(subJson1.data)[-1]["email"]
            print(xc)
            return Response(xc+" Added to "+xc1, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################  Getting Names      #################################

##### place  #######

@api_view(["GET","POST"])
def placenamelist(request):
    if request.method == "GET":
        device_data = place.objects.filter(p_id=request.GET['p_id'])
        nameJson = placenameSerializers(device_data, many=True)
        # return Response(nameJson.data)
        # dd = list(nameJson.data)[0]["p_type"]
        # print(dd)
        return Response(nameJson.data)

##### floor  #######



##### flat  #######

################  User can get all data added by him  ####################
@api_view(["GET"])
def tempulist(request):
    if request.method == "GET":
        device_data = tempuser.objects.filter(user=request.user)
        nameJson = tempuserregisterSerializers(device_data, many=True)
        return Response(nameJson.data)

############### Registring temporary user by main user  ##############

                            ########## Auto delete Temporary User  ####################

@api_view(["GET","POST","DELETE"])
def tempU(request):
    if request.method == "GET":
        device_data = tempuser.objects.filter(mobile=request.GET['mobile'])
        nameJson = tempuserregisterSerializers(device_data, many=True)
        return Response(nameJson.data)
    elif request.method == "POST":
        tempdata = tempuserregisterSerializers(data=request.data)
        if tempdata.is_valid():
            tempdata.save()
            return Response("Temporary User is now active.", status=status.HTTP_201_CREATED)
        return Response(tempdata.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # received_json_data=json.loads(request.body)
        # if received_json_data['id']=='p_id':
        try:
            data = tempuser.objects.filter(mobile=request.GET['mobile'], p_id=request.GET['p_id'])
            #print(data)
            data.delete()
        except Exception:
            print("p_id not found")
            pass

        try:
        # elif received_json_data['id']=='f_id':
            data2 = tempuser.objects.filter(mobile=request.GET['mobile'], f_id=request.GET['f_id'])
            data2.delete()
        except Exception:
            print("f_id not found")
            pass
        # elif received_json_data['id']=='r_id':

        try:
            data3 = tempuser.objects.filter(mobile=request.GET['mobile'], r_id=request.GET['r_id'])
            data3.delete()
        
        # elif received_json_data['id']=='d_id':
        except Exception:
            print("r_id not found")
            pass
        try:
            data4 = tempuser.objects.filter(mobile=request.GET['mobile'], d_id=request.GET['d_id'])
            data4.delete()
        except Exception:
            print("d_id not found")
            pass

        # else:
        #     print("not found")
        # data2 = tempUserVerification.objects.filter(mobile=request.GET['mobile']) or tempUserVerification.objects.filter(email=request.GET['email'])
        # data3 = otptemplogin.objects.filter(mobile=request.GET['mobile']) or otptemplogin.objects.filter(email=request.GET['email'])
        # data2.delete()
        # data3.delete()
        return Response("Temporary User has no longer Exists.")



@api_view(["GET"])
def subuplaceget(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(user=request.user)
        placeJson = subuserplacegetSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

@api_view(["GET"])
def subuserfind(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(user=request.user)
        dataJson = subuserplaceSerializers(data, many=True)
        return Response(dataJson.data)

@api_view(["GET"])
def subuserfindsubuser(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(email=request.GET['email'])
        dataJson = subuserplaceSerializers(data, many=True)
        return Response(dataJson.data)


def send_otp(mobile , otp):
    print("FUNCTION CALLED")
    x = otp
    y = mobile
    n = '+91'
    account_sid = 'ACd6173a93be390fe7eb1f2bf7faceeb0e'
    auth_token = '4892323294c8cc241e2107380b0c3f59'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='Your OTP is ' + x + '. Please add this OTP to login field as directed.\n' + 'THANK YOU for using GENORION.',
                                from_='+12095887091',
                                to=n+y
                            )
    print(message.sid)
    print(x)
    # return super().save(*args, **kwargs)
    return None
@api_view(["GET","POST","DELETE"])
def tempu(request):
    if request.method == "POST":
        form = TemporaryUserForm(request.POST)
    # print(request.POST)
    # print(form)
        if form.is_valid():
            form.save()
            number = tempUserVerification.objects.filter()
            subJson1 = otpfortampuserSerializers(number, many=True)
            
            
            # success = False
            # for x in list(subJson1.data):
            mobile1 = list(subJson1.data)[-1]["mobile"]
            otp = list(subJson1.data)[-1]["otp"]
            if tempuser.objects.filter(mobile=mobile1).exists():
                print(mobile1)
                print(otp)
                send_otp(mobile1, otp)
            # request.session['mobile'] = mobile
                return Response("Otp Sent to your mobile number.", status=status.HTTP_201_CREATED)
            else:
                deletetemp = tempUserVerification.objects.last()
                print(deletetemp)
                deletetemp.delete()
                return Response("number does not exists.")
        else :
        # return JsonResponse({"Password is too similar"})
            print(form.errors.as_json())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR ,data=form.errors.as_json())
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

 #############################################################################################################################################                
 #############################################################################################################################################                
  



###################################        website urls          #####################################


from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request,'login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                userlogin(request,user)
                return redirect('/')
        else:
            context = {
                "form":form
            }
            return render(request,'login.html',context)
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)