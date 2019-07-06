from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from teacher.models import course,session
from .models import student, project, file
from customuser.models import  user_type
from django.core.files.storage import FileSystemStorage
from .forms import fileform
# Create your views here.


def shome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        #Gets project details and creates a project.
        if request.method == 'POST':
            project_title = request.POST.get('project-title')
            group_name = request.POST.get('group-name')
            course_code = course.objects.get(course_code=request.POST.get('course-list'))
            session_val = session.objects.get(batch=request.POST.get('session-list'))
            project_id = project_title+session_val.batch+session_val.course_code
            #print(course_code.course_code)

            member_data_string = request.POST.get('my_data')
            members = member_data_string.split(',')
            member_reg = []
            for val in members:
                reg = ""
                for c in val:
                    if c >= '0' and c <= '9':
                        reg = reg + c
                    else:
                        member_reg.append(student.objects.get(reg_number=reg))
                        break

            def_mem = student.objects.get(reg_number='000')
            if len(member_reg) == 1:
                prj = project(project_title=project_title, group_name=group_name, course_code=course_code, session=session_val,
                            member1_reg=member_reg[0], member2_reg=def_mem, member3_reg=def_mem, project_id=project_id)
                prj.save()
            elif len(member_reg) == 2:
                prj = project(project_title=project_title, group_name=group_name, course_code=course_code, session=session_val,
                            member1_reg=member_reg[0], member2_reg=member_reg[1], member3_reg=def_mem, project_id=project_id)
                prj.save()
            elif len(member_reg) == 3:
                prj = project(project_title=project_title, project_id = project_id, group_name=group_name, course_code=course_code, session=session_val,
                            member1_reg=member_reg[0], member2_reg=member_reg[1], member3_reg=member_reg[2])
                prj.save()

        projects_ob = project.objects

        return render(request, 'student/student-home.html', {'projects': projects_ob})

    else:
        print("STUDENT NA")
        return HttpResponse(request, '<h1>STUDENT NA</h1>')

def load_sessions(request):
    course_code = request.GET.get('course_code')
    sessions = session.objects.filter(course_code=course_code)
    return render(request, 'student/session-dropdown-options.html', {'sessions': sessions})

def newproject(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        course_ob = course.objects
        session_ob = session.objects
        student_ob = student.objects.exclude(reg_number='000')
        return render(request, 'student/new-project.html', {'course':course_ob, 'student':student_ob, 'sessions':session_ob})
    else:
        print("STUDENT NA")
        return HttpResponse(request, '<h1>STUDENT NA</h1>')

def projectdetails(request, project_id):
    #print(project_title, session)
    if request.method == 'POST':
        for uploaded_file in request.FILES.getlist('file'):
            #uploaded_file = request.FILES['file']
            # fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)

            project_ob = project.objects.get(project_id=request.POST.get("project_id"))
            file_obj = file(file_name=uploaded_file.name, project_id=project_ob, file_content=uploaded_file)
            file_obj.save()

    files = file.objects
    project_obj = get_object_or_404(project, pk=project_id)
    return render(request, 'upload.html', {'project_obj':project_obj,'files':files})


# def delete_file(request, pk):
#     if request.method == 'POST':
#         file_obj = file.objects.get(file, pk = pk)
#         file_obj.delete()
#     return redirect('upload.html')