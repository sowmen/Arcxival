from django.shortcuts import render
from teacher.models import course, session, teacher
from django.core import serializers

# Create your views here.

def thome(request):
    if(request.method == 'POST'):
        course_code = course.objects.get(course_code=request.POST.get('course-code-list'))
        batch = request.POST.get('batch')
        date = request.POST.get('start-date')
        t_code = teacher.objects.get(teacher_code='MSI')

        sn = session(course_code=course_code, batch=batch, date=date, teacher_code=t_code)
        sn.save()

        with open("file.json", "w") as out:
            json_serializer = serializers.get_serializer('json')()
            json_serializer.serialize(session.objects.all(), stream=out)

    return render(request, 'teacher/teach-home.html')

def createsession(request):
    if(request.method == 'POST'):
        course_code = request.POST.get('course-code')
        course_title = request.POST.get('course-title')
        credit = request.POST.get('credit-input')
        t_code = teacher.objects.get(teacher_code='MSI')
        c = course(course_code=course_code, course_title=course_title, course_credit=credit, teacher_code=t_code)
        c.save()

    course_obj = course.objects
    return render(request, 'teacher/create-session.html', {'courses':course_obj})