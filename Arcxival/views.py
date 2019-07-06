from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings

def home(request):
    if(request.method == 'POST'):
        print("ashche")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = get_user_model(email=email, password=password)
        print("now")
        if user is not None:
            if user.is_active:
                print("HERE")
    return render(request, 'home.html')

# def signup(request):
#     return HttpResponse(request, '<h1>IN SIGNUP</h1>')
#
# def signup_student(request):
#     return HttpResponse(request, '<h1>IN STUDENT</h1>')
#
# def signup_teacher(request):
#     return HttpResponse(request, '<h1>IN TEACHER</h1>')