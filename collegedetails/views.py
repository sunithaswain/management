from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image,Contact
from .forms import Registerform,Signinform,changeform,Uploadform,contactform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as signout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
def login(request):
    ''' Login '''

    error_message = ""
    if request.method == 'POST':
        form = Signinform(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        # request.POST['password']
        if form.is_valid():
            user = authenticate(username=user_name, password=password)        
            print ("valid")
            auth_login(request, user)
            user_id=User.objects.get(username=user_name).id
            print (user_id)
            return redirect("/details/userprofile/%d"%user_id)
            
    else:
        form = Signinform()
    return render(request, 'login.html', {'form': form, 'error_message':error_message,})

def regisin(request):
    username=Email=password=Mobilenumber=Address=""
    success_message = ""
    if request.method == "POST":
        form = Registerform(request.POST)
        print ('post method')
        if form.is_valid():
            print ('if form is valid')

            username = request.POST.get('username') 
            Email = request.POST.get('Email')            
            password = request.POST.get('password')
            Mobilenumber = request.POST.get('Mobilenumber')
            Address = request.POST.get('Address')

            user = User.objects.create_user(username=username,Email=Email,password=password,Mobilenumber=Mobilenumber,Address=Address)
            
            # user.save()
            success_message = "User successfully created"

        else:
            print('not valid form')
    else:
        print ('else condition')
        form = Registerform()
        print()
    return render(request, 'register.html', {'form':form, 'message':success_message,'username':username,'Email':Email,'password':password,'Mobilenumber':Mobilenumber,'Address':Address})
# __init__.py

def content(request):
    # form_class = contactform()
    success_message = ""
    print ('contact form view')
    if request.method == "POST":
        form_class = contactform(request.POST)
        print ('post method')
        if form_class.is_valid():
            print ('if form is valid')

            username1 = request.POST.get('user_name') 
            email1 = request.POST.get('email')  
            project1 = request.POST.get('projectdetails')  
            print (username1)           
            print (email1)
            contact = Contact.objects.create(yourname=username1,emailAdress=email1,projectdetails=project1)
            
            success_message = 'Contact details successfully submitted'
    else:
        print ('else condition')
        form_class = contactform()
        print(form_class)
    return render(request, 'contact.html', {'form':form_class, 'message':success_message})
    
def indexing(request):
     #this definition for home page 

    message = "Welcome To Homepage"
    
    return render(request, "index.html", {'welcome_message':message}) 
def profiling(request, user_id):
     #this definition for home page 
    print ('profile view')
    user_id = User.objects.filter(id=user_id) 
    upload_file_url = ""
    u_id = ""
    for i in user_id:
        u_name = i.username
        pwd = i.password
        u_id = i.id

    imagedetails = Image.objects.filter(user_id=request.user.id)
    if imagedetails:
        for i in imagedetails:
            upload_file_url = i.image
            print (upload_file_url)

    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        image1=request.FILES.get('image')
        profile_image = Image.objects.create(user_id=request.user.id,image=image1)
        profile_image.save()

        


    else:
        form = Uploadform()

    
    


    message = "Welcome To Homepage"
    
    return render(request, "profile.html", {'username':u_name, 'password':pwd, 'form':form,
        'profile_image':upload_file_url})   

def logoutin(request):

    signout(request)
    return redirect('/details/')

def changingpassword(request):
    print (request.user.id)
    print (request.user.username)

    error_message = ""
    if request.method == 'POST':
        form = changeform(request.POST)
        user_name = request.POST.get('oldpassword')
        password = request.POST.get('newpassword')
        # request.POST['password']
        if form.is_valid():    
            # User.objects.get(username='john')        
            user=User.objects.get(username=request.user.username)
            # u.set_password('new password')
            user.set_password(password)
            
            user.save()
            error_message = "paasword changed successfully"
    else:
        form=changeform()
    return render(request, 'changepass.html', {'msge':error_message})
def email(request):
    success_message = ""
    if request.method == 'POST':
        form = emailform(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #to_email = request.POST.get('from_email', '')
        #from_email = 'sunithaswain20@gmail.com'
        if username and password:
            try:
                send_mail(username, password,fail_silently=False,)
                success_message = "Email sent successfully"
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponseRedirect('/contact/thanks/')

            return render(request,'email.html', {'form':form, 'message':success_message})
        else:
            form = emailform()
            error_message = "Make sure all fields are entered and valid."
            return render(request,'email.html', {'form':form, 'message':error_message})
def home(request):
    return render(request, 'home.html')