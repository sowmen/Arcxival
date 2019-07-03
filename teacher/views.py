from django.shortcuts import render
from teacher.models import course

# Create your views here.

def thome(request):
    return render(request, 'teacher/teach-home.html')

def createsession(request):
    if(request.method == 'POST'):
        course_code = request.POST.get('course-code')
        course_title = request.POST.get('course-title')
        credit = request.POST.get('credit-input')
        c = course(course_code=course_code, course_title=course_title, course_credit=credit)
        c.save()

    course_obj = course.objects
    return render(request, 'teacher/create-session.html', {'courses':course_obj})