from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class loc_user(AbstractBaseUser):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True) 
    #created_at=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    
    def __str__(self):
        return self.username

    #custom authenticate method

    @property
    def is_authenticated(self):
        return True
    
class Product_Category(models.Model):
    Category=models.CharField(max_length=100)

    def __str__(self):
        return self.Category    
    
class Products(models.Model):
    image=models.ImageField(upload_to="media")    


'''class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_course=models.CharField(max_length=50)
    teacher=models.ForeignKey(loc_user,on_delete=models.CASCADE,related_name="employee")'''

