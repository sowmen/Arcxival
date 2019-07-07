from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.conf import settings
from customuser.models import user_type
from teacher.models import course, session
from student.models import project, file


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

def archive_courses(request):
    courses = course.objects
    print(courses)
    return render(request, 'archive_courses.html', {'courses': courses})

def archive_Sessions(request, pk):

    print("here",pk)
    session_obj = session.objects.filter(course_code_id=pk);
    print(session_obj)
    return render(request, 'archive_Sessions.html', {'sessions':session_obj})

def archive_Projects(request,pk):

    project_ob = project.objects.filter(session_id=pk)
    return render(request, 'archive_Projects.html.', {'projects':project_ob})

def projectdetails(request, session_id, project_id):
    #print(project_title, session)
    if request.user.is_authenticated:
        if request.method == 'POST':
            for uploaded_file in request.FILES.getlist('file'):
                #uploaded_file = request.FILES['file']
                # fs = FileSystemStorage()
                # fs.save(uploaded_file.name, uploaded_file)

                project_ob = project.objects.get(project_id=request.POST.get("project_id"))
                file_obj = file(file_name=uploaded_file.name, project_id=project_ob, file_content=uploaded_file)
                file_obj.save()

        print("there", project_id)
        files = file.objects
        project_obj = get_object_or_404(project, pk=project_id)
        return render(request, 'upload.html', {'project_obj':project_obj,'files':files})
    else:
        print("TEACHER BA STUDENT NA")
        return HttpResponse(request, '<h1>TEACHER BA STUDENT NA</h1>')
