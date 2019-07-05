from django.shortcuts import render, get_object_or_404
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

    sessions_obj = session.objects.order_by('course_code','batch')
    return render(request, 'teacher/teach-home.html', {'sessions': sessions_obj})

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

def batchinfo(request, batchno):
    batch_obj = get_object_or_404(session, pk=batchno)
    print(batch_obj)
    return render(request, 'teacher/batch-details.html', {'batch_obj': batch_obj})