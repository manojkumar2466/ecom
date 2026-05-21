from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, LoginForm, UserUpdateForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():          
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Verify your email to activate your account"
            message = render_to_string("users/email_verification.html",{
                "user":user,
                "domain":current_site.domain,
                "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                "token":account_activation_token.make_token(user),
            })
            user.email_user(subject=subject,message= message)
            return redirect("email_verification_sent")

    context ={
        "form":form,
    }
    return render(request, "users/register.html", context)

def user_login(request):
    print("login function")
    form = LoginForm()
    if request.method=="POST":
        print("login post request")
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("myapp:index")


    context= {
        "form":form,
    }
    return render(request,"users/login.html",context)

def user_logout(request):
    logout(request)
    return redirect("login")

def profile(request):
    if request.method=="POST":
        form = UserUpdateForm(data=request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect("myapp:index")
    update_form = UserUpdateForm(instance=request.user)
    context = {
        "update_form":update_form
    }
    return render(request,"users/profile.html",context)

def email_verification(request, uidb64, token):
    id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=id)
    if user and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect("email_verification_success")
    else:
        return redirect("email_verification_failed")

   

def email_verification_sent(request):
   return render(request, "users/email_verification_sent.html")

def email_verification_success(request):
   return render(request,"users/email_verification_success.html")

def email_verification_failed(request):
   return render(request, "users/email_verification_failed.html")

#bfai apfe rcwg gfej