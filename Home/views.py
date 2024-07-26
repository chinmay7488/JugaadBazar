from django.shortcuts import render, redirect
from Home.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
User = get_user_model()

# Create your views here.

def Home(request):

    query_set = Product.objects.all()


    return render(request,'home.html', context={'products': query_set})

def login_page(request):

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        if not User.objects.filter(phone_number=phone_number).exists():
            messages.add_message(request, messages.error, "Invaild Phone Number")
            return redirect("/login/")

        user = authenticate(phone_number=phone_number, password = password)
        if user is None:
            messages.add_message(request, messages.ERROR, "Invaild Password")
        else:
            login(request, user)
            return redirect("/")
        return redirect("/login/")

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        if not User.objects.filter(phone_number=phone_number).exists():
            messages.add_message(request, messages.error, "Phone Number already exists")
            return redirect("/login/")
        else:
            user = User.objects.create(
                    full_name = full_name,
                    email = email,    
                    phone_number = phone_number,  
                        )
            user.set_password(password)
            user.save()
            messages.add_message(request, messages.INFO, "Register Successful")
            return redirect("/login/")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')