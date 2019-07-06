from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.conf import settings
from customuser.models import user_type

def home(request):
    if(request.method == 'POST'):
        print("ashche")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print("now")
        if user is not None:
            login(request, user)
            print("HERE")
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('shome')
            elif user.is_authenticated and type_obj.is_teach:
                return redirect('thome')
        else:
            print("PAI NAI")
            return redirect('home')

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')