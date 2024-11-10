from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .models import loc_user,Employee
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# home page 
def Home(request):
    
    '''dashboard data count and check for user authenticated because if the user logout the data value become 0'''
    
    if request.user.is_authenticated:
        emp_data=Employee.objects.filter(teacher_id=request.user)
        data=emp_data.count()
    else:
        data="0"    

    context={
        'count':data
    }
    return render(request,'index.html',context)

def Signin(request):
    #post method to get the data from signin form
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        
        # if successfuly match the username and password 
        user= authenticate(request,username=name,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"wrong username and password")
            return redirect('signin')
        
    return render(request,'signin.html')

def Signup(request):  
    # post method to get the signup data   
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirm=request.POST.get('password2')
        print(name,email,password,confirm)
       
        # check for if password does not match
        if password!=confirm:
            messages.error(request,"password not match")
            return redirect('signup')
            
        # if both the password is same     
        else:

            # if the username already exist
            if loc_user.objects.filter(username=name).exists():
                messages.error(request,"username already exist")
                return redirect('signup')
            
            # if username not exist 
            else:
                hash_password=make_password(password)
                d=loc_user.objects.create(username=name,email=email,password=hash_password)
                d.save()
                messages.success(request,"successfully signup")

                #email sending code
                #subject="welcome"
                #message="successfuly sign in"
                #from_email=settings.EMAIL_HOST_USER
                #Reciepient_list=["puspendrarajput746@gmail.com"]
                #send_mail(subject,message,from_email,Reciepient_list)

                return redirect('signin')


    return render(request,'signup.html')

# signout user 
def Signout(request):
    logout(request)
    return redirect('home')

# dashoard to show the data
def Dashboard(request):
    #show only the login user related data by using filter
    data=Employee.objects.filter(teacher_id=request.user)

    '''dashboard data count and check for user authenticated because if the user logout the data value become 0'''
    
    if request.user.is_authenticated:
        emp_data=Employee.objects.filter(teacher_id=request.user)
        count=emp_data.count()
    else:
        count="0"    

    return render(request,'dashboard.html',{'data':data,'count':count})

#delete the data by clicking the btn 
def Delete(request,id):
    data=get_object_or_404(Employee,id=id)
    data.delete()
    return redirect('dashboard')

#Ad employee detail
def Add_emp(request):
    # employee form data 
    if request.method=="POST":
        emp_name=request.POST.get('emp_name')
        emp_email=request.POST.get('emp_email')
        emp_course=request.POST.get('emp_course')
        d=Employee(emp_name=emp_name,emp_email=emp_email,emp_course=emp_course,teacher=request.user)
        d.save()


    '''dashboard data count and check for user authenticated because if the user logout the data value become 0'''
    
    if request.user.is_authenticated:
        emp_data=Employee.objects.filter(teacher_id=request.user)
        count=emp_data.count()
    else:
        count="0"   
    return render(request,'add_employee.html',{'count':count})

def Show_products(request):
    return render(request,'Products.html')


    
