from django.shortcuts import render, get_object_or_404
from teacher.models import course, session, teacher
from django.core import serializers
from customuser.models import user_type


# Create your views here.

def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        if(request.method == 'POST'):
            course_code = course.objects.get(course_code=request.POST.get('course-code-list'))
            batch = request.POST.get('batch')
            session_id = course_code.course_code + batch
            date = request.POST.get('start-date')
            t_code = teacher.objects.get(email=request.user)
            print(t_code.teacher_code)

            sn = session(course_code=course_code, batch=batch, session_id=session_id, date=date, teacher_code=t_code)
            sn.save()

            with open("file.json", "w") as out:
                json_serializer = serializers.get_serializer('json')()
                json_serializer.serialize(session.objects.all(), stream=out)

        teacher_id = teacher.objects.get(email=request.user)
        print(teacher_id.teacher_code)
        sessions_obj = session.objects.filter(teacher_code=teacher_id.teacher_code)
        return render(request, 'teacher/teach-home.html', {'sessions': sessions_obj})
    else:
        print("TEACHER NA")

def createsession(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        if(request.method == 'POST'):
            course_code = request.POST.get('course-code')
            course_title = request.POST.get('course-title')
            credit = request.POST.get('credit-input')
            t_code = teacher.objects.get(email=request.user)
            c = course(course_code=course_code, course_title=course_title, course_credit=credit, teacher_code=t_code)
            c.save()

        course_obj = course.objects
        return render(request, 'teacher/create-session.html', {'courses':course_obj})
    else:
        print("TEACHER NA")

def batchinfo(request, session_id):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        batch_obj = get_object_or_404(session, pk=session_id)
        print(batch_obj)
        return render(request, 'teacher/batch-details.html', {'batch_obj': batch_obj})
    else:
        print("TEACHER NA")