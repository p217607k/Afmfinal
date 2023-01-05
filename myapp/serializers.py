
from django.db.models import fields
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
# from drf_braces.serializers.form_serializer import FormSerializer
# from myapp.forms import UserRegisterForm, SubUserRegisterForm
from myapp.models import( deviceStatus, place,field,device, subuseraccess, subuserplace, tempuser,allDevices,FirebaseDetails
   ,phone,emergencyNumber,ssidPassword,pinschedule,tempUserVerification,exl_files)
class phone_Serializers(serializers.ModelSerializer):
    class Meta:
        model = phone
        fields = '__all__'
##
class exlSerializers(serializers.ModelSerializer):
    class Meta:
        model = exl_files
        fields = '__all__'
##
class otploginSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempUserVerification
        fields = '__all__'
###
class otpfortampuserSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempUserVerification
        fields = '__all__'
###
class pinscheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = pinschedule
        fields = '__all__'
##
class ssidPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = ssidPassword
        fields = '__all__'
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class userlogingetdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

# class emailSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email',)

# class firstnameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name',)

class subuseremailSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuseraccess
        fields = ('emailtest',)

#_fr= SubUserRegisterForm

class placeSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = '__all__'

class placenameSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = ('p_type','p_id')


class fieldSerializers(serializers.ModelSerializer):
    class Meta:
        model = field
        # fields = ('f_id', 'f_name')
        fields = '__all__'

class fieldnameSerializers(serializers.ModelSerializer):
    class Meta:
        model = field
        fields = ('f_name','f_id')

# class flatSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = flat
#         # fields = ('f_id', 'f_name')
#         fields = '__all__'

# class flatnameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = flat
#         fields = ('flt_name','flt_id')


class allDeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = allDevices
        fields = '__all__'

# class roomnameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = room
#         fields = ('r_name','r_id')


class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'




class subuseraccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuseraccess
        fields = '__all__'


class subuserplaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = '__all__'

class subuserplacegetSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = ('name','email', 'p_id',)

# class otploginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = tempUserVerification
#         fields = '__all__'


# # class ValidatePhoneSendOTPSerializers(serializers.ModelSerializer):
# #     class Meta:
# #         model = PhoneOTP
# #         fields = '__all__'

class tempuserregisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= '__all__'

class dateasignSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= ('id','date','timing',)

# class timeasignSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = tempuser
#         fields= ('timing',)


# class otpfortampuserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = tempUserVerification
#         fields = '__all__'

# class otpuserloginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = otptemplogin
#         fields = '__all__'

class FirebaseSer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseDetails
        fields = '__all__'


# class energySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = energy
#         fields = '__all__'

# class onehourenSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = oneHourEnergy
#         fields = '__all__'


# class oneyearenSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = oneyeardata
#         fields = '__all__'    

# class threeyearenSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = threeyears
#         fields = '__all__'     



# # from .models import employees

# # class employeesSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = employees
# #         fields = '__all__'
class deviceStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = deviceStatus
        fields = '__all__'
        ########
class emernumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = emergencyNumber
        fields = '__all__'
# from .models import post
# from .models import post
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class PostSer(serializers.ModelSerializer):
    class Meta:
        # model = post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]



#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 
          'first_name', 'last_name','email','password', 'password2')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user