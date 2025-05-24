from django.db import models

# Create your models here.

class Faculty(models.Model):
   GENDER_CHOICES=[
      ("MALE","MALE"),
      ("FEMALE","FEMALE")
   ]
   teacher_id = models.CharField(max_length=10, primary_key=True)
   profile_picture = models.ImageField(upload_to='images', blank=True, null=True)
   name = models.CharField(max_length=100)
   gender = models.CharField(choices=GENDER_CHOICES, max_length=6,default="")
   dob = models.DateField()
   email = models.EmailField(max_length=100, unique=True)
   age = models.IntegerField()
   date_of_joining = models.DateField()
   experience = models.IntegerField()
   designation = models.CharField(max_length=100)
   department = models.CharField(max_length=100)
   salary = models.IntegerField()
   contact_number = models.CharField(max_length=15)
   address = models.TextField()
   qualification = models.CharField(max_length=100)
   
   
   def _str_(self):
        return self.name



