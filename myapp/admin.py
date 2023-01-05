from django.contrib import admin
# Register your models here.
# from embed_video.admin import AdminVideoMixin
# from .models import Videos
# from .models import employees
from django.contrib import admin
from . models import *

@admin.register(place)
class lace(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(field)
class CusAdmin(admin.ModelAdmin):
    list_display= ('id',)
admin.site.register(allDevices)
admin.site.register(pinschedule)
admin.site.register(tempUserVerification)


admin.site.register(exl_files)

admin.site.register(device)

admin.site.register(deviceStatus)
admin.site.register(emergencyNumber)
admin.site.register(ssidPassword)
# admin.site.register(pinName)
admin.site.register(subuseraccess)


admin.site.register(subuserplace)
admin.site.register(tempuser)
admin.site.register(FirebaseDetails)



# class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
#     pass

# admin.site.register(Videos, MyModelAdmin)

# admin.site.register(employees)
