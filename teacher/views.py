from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from teacher.models import course, session, teacher
from student.models import project, file
from django.core import serializers
from customuser.models import user_type


# Create your views here.

def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        if (request.method == 'POST'):
            if request.POST.get('end_session') is not None:
                ssn = request.POST.get('session')
                ob = session.objects.get(session_id=ssn)
                ob.running = False
                ob.save()
                print(session.objects.get(session_id=ssn).running)
                # session.objects.get().running = False
            else:
                course_code = course.objects.get(course_code=request.POST.get('course-code-list'))
                batch = request.POST.get('batch')
                session_id = course_code.course_code + batch
                date = request.POST.get('start-date')
                t_code = teacher.objects.get(email=request.user)
                print(t_code.teacher_code)
                if course_code and batch and session_id and date and t_code:
                    sn = session(course_code=course_code, batch=batch, session_id=session_id, date=date,
                                 teacher_code=t_code)
                    sn.save()

        teacher_id = teacher.objects.get(email=request.user)
        print(teacher_id.teacher_code)
        sessions_obj = session.objects.filter(teacher_code=teacher_id.teacher_code)
        data = []

        for x in sessions_obj:
            tit = course.objects.get(course_code=x.course_code.course_code).course_title
            data.append({'session': x, 'title': tit})
        print(data)

        type = "teach"
        return render(request, 'teacher/teach-home.html', {'data': data, 'type':type})
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('shome')
    else:
        return redirect('home')


def createsession(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        if (request.method == 'POST'):
            course_code = request.POST.get('course-code')
            course_title = request.POST.get('course-title')
            credit = request.POST.get('credit-input')
            t_code = teacher.objects.get(email=request.user)
            if course_code and course_title and credit:
                c = course(course_code=course_code, course_title=course_title, course_credit=credit,
                           teacher_code=t_code)
                c.save()

        course_obj = course.objects

        type = "teach"
        return render(request, 'teacher/create-session.html', {'courses': course_obj, 'type':type})
    else:
        if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
            return redirect('shome')


def batchinfo(request, session_id):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        session_obj = get_object_or_404(session, pk=session_id)
        print(session_obj.session_id)
        project_objs = project.objects.raw("select * from student_project where session_id LIKE %s",
                                           [session_obj.session_id])

        type = "teach"
        return render(request, 'teacher/teacher_projects.html', {'projects': project_objs, 'session': session_obj, 'type':type})
    else:
        if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
            return redirect('shome')


def projectdetails(request, session_id, project_id):
    # print(project_title, session)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('delete') is not None:
                path = request.POST.get('delete')
                print(path)
                full_path = os.path.join(settings.MEDIA_ROOT, path)
                full_path = full_path.replace("/", "\\")
                print(full_path)
                try:
                    os.remove(full_path)
                except FileNotFoundError:
                    return redirect(request.path_info)

                fileob = file.objects.get(file_content=request.POST.get('delete'))

                fileob.delete()


            else:
                for uploaded_file in request.FILES.getlist('file'):
                    # uploaded_file = request.FILES['file']
                    # fs = FileSystemStorage()
                    # fs.save(uploaded_file.name, uploaded_file)
                    size = uploaded_file.size

                    ext = ""
                    if size < 512000:
                        size = size / 1024.0
                        ext = 'Kb'
                    elif size < 4194304000:
                        size = size / 1048576.0
                        ext = 'Mb'
                    else:
                        size = size / 1073741824.0
                        ext = 'Gb'
                    value = '%.2f' % size
                    value = value + ext
                    # print(value)
                    project_ob = project.objects.get(project_id=request.POST.get("project_id"))
                    file_obj = file(file_name=uploaded_file.name, project_id=project_ob, file_content=uploaded_file,
                                    file_size=value)
                    file_obj.save()

        files = file.objects
        project_obj = get_object_or_404(project, pk=project_id)

        type = ""
        if user_type.objects.get(user=request.user).is_teach:
            type = "teach"
        else:
            type = "student"
        return render(request, 'upload.html', {'project_obj': project_obj, 'files': files, 'type':type})
    else:
        return redirect('home')
