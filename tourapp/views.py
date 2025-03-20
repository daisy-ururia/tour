from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from tourapp.models import *



# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def elements(request):
    return render(request, 'elements.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        mycontact = contact2 (
        fname= request.POST ['fname'],
        lname= request.POST ['lname'],
        email= request.POST ['email'],
        message = request.POST['message']
        )
        mycontact.save()
        return redirect('/success')

    else:
        return render(request,'contact.html')

def success(request):
    return render(request, 'success page.html')

def search(request):
    if request.method == 'POST':
        mysearch = searches (
        select= request.POST ['select'] ,
        daterange= request.POST ['daterange'] ,
        people= request.POST ['people']
        )
        mysearch.save()
        return redirect('/services')

    else:
        return render(request, 'index.html')


def signup(request):
    """ Show the registration form """
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        # Check the password
        if password == password:
            try:
                user = User.objects.create_user(name=name,phone=phone, email=email, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/index')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        # Check if the user exists
        if email is not None:
            # login(request, user)
            login(request,email)
            return redirect('/index')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'index.html')


