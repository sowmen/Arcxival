from django.shortcuts import render
from teacher.models import course,session
from .models import student

# Create your views here.

def shome(request):
    return render(request, 'student/student-home.html')


def newproject(request):
    course_ob = course.objects
    session_ob = session.objects
    student_ob = student.objects
    return render(request, 'student/new-project.html', {'course':course_ob, 'session':session_ob, 'student':student_ob})