
from django.contrib import admin
from Registration.models import Registration_Info, UserProfile

# Register your models here.


class Registration_Info_Admin(admin.ModelAdmin):
    list_display = ('College_Name', 'Number_of_Participants' ,  'Contact', 'Email', 'Address', 'Date' )
admin.site.register(Registration_Info, Registration_Info_Admin)





class UserProfile_Admin(admin.ModelAdmin):
    list_display = ('user', 'committee', 'post', 'Roll_No', 'phone' )

admin.site.register(UserProfile, UserProfile_Admin)






admin.site.site_header = 'Welcome To Administration'
