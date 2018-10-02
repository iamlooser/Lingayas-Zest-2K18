from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
            user = models.OneToOneField(User,on_delete=models.CASCADE)
            committee = models.CharField(max_length=30,blank='True',null='True')
            post = models.CharField(max_length=30,blank='True',null='True')
            Roll_No = models.CharField(max_length=10,blank='True',null='True')
            phone = models.CharField(max_length=10,blank='True',null='True')

            def __unicode__(self):
                return self.Roll_No
            def  __str__(self):
                return self.committee








class Registration_Info(models.Model):
    College_Name = models.CharField(max_length=250)
    Number_of_Participants= models.IntegerField()
    Email = models.EmailField(blank=False, null=True)
    Contact = models.CharField(max_length=10, null=True, blank=False)
    Address = models.TextField(null=True, blank=False)
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.Collage_Name

    class Meta:
        managed = True
        db_table = 'website_feedback_database'
