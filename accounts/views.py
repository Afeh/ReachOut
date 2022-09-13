from email import message
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
            #return redirect("login")
    
    return render(request, "register.html", {"form": form})