from django.shortcuts import render, HttpResponse
from .models import Student, Category,Subcategory,Landing,Logo,VideoBanner
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token, TokenGenerator
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Category
# Create your views here.
def index(request):
    dests = Category.objects.all()
    land = Landing.objects.all()[:7] 
    logo = Logo.objects.first()
    vid = VideoBanner.objects.first()
    return render(request, 'josh.html', {'dests': dests, 'land': land, 'logo':logo, 'vid':vid})


class CategoryDetailView(View):
    template_name = 'category.html'

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        subcategories = category.categories.all()
        return render(request, self.template_name, {'category': category, 'subcategories': subcategories})

def register(request):
    if request.method == "POST":
        name =request.POST['name']
        tel =request.POST['telephone']
        email = request.POST['email'] 
        place = request.POST['place']
        gen = request.POST['gender']
        status = request.POST['employment']
        obj=Student()
        obj.name=name
        obj.tel=tel
        obj.email=email
        obj.place=place
        obj.gen=gen
        obj.status=status
        obj.save()
        return HttpResponse("<h2>Thank you For Registering With Jonjo Fashions</h2>")
    return render(request, 'index.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')
        
        try:
            if User.objects.get(username=email):
               messages.info(request, "Email is Taken")
               return render(request, 'signup.html') 
              
               
        except Exception as identifier:
            pass     
        
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save() 
        email_subject="Activate Your Account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
            
        })
        email_message = EmailMessage(email_subject, message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,"Activate your Account by clicking the link in your gmail")
        return redirect('/login/')
    return render(request, "signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
        
    return render(request, "login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as Identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):   
            user.is_active=True
            user.save()
            messages.info(request, "Account Activated Successfully")
            return redirect('/auth/login')    
        return render(request,'activatefail.html')
    
    
     
