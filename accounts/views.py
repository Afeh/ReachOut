from email import message
import email
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_user(request):
    form = CustomUserCreationForm()

    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            email = request.POST["email"]
            subject = "Welcome to ReachOut!"
            message = f'Hi {first_name} welcome to ReachOut. Nice to have you here.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            messages.info(request, "Account successfully created. You can now login.")
            return redirect("login")
    
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":

        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)

        if user is not None:
            form = login(request, user)
            return redirect('index')
        
        else:
            messages.info(request, f' Account does not exist, please signup')
            return redirect('signup')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':login})
