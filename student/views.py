from django.shortcuts import render
from teacher.models import course,session
from .models import student

# Create your views here.

def shome(request):
    return render(request, 'student/student-home.html')


def newproject(request):
    if request.method == 'POST':
        project_title = request.POST.get('project-title')
        group_name = request.POST.get('group-name')
        course_code = request.POST.get('course-list')
        session_val = request.POST.get('session-list')
        members = request.POST.getlist('member-list')

        s = student(project_title = project_title, group_name=group_name, course_code=course_code, session=session_val, members=members)
        s.save()

    course_ob = course.objects
    session_ob = session.objects
    print("Here: ")
    print(len(session.objects.all()))
    student_ob = student.objects.exclude(reg_number='000')
    return render(request, 'student/new-project.html', {'course':course_ob, 'student':student_ob, 'sessions':session_ob})