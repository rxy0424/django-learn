# -*- coding : utf-8 -*-
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post,Homework,Homeworkansower,Discuss,Discussreplay

from django.contrib.auth.decorators import login_required

from django.contrib import auth

from .models import Student,Subjectfile

from django.contrib.auth.models import User

from django.http import StreamingHttpResponse

from django import forms

from django.template import RequestContext


# Create your views here.


class FileForm(forms.Form):
    file = forms.FileField()

@login_required
def index(request):
    posts_list = Post.objects.order_by('-update_time')[:5]
    homework_list = Homework.objects.order_by('-update_time')[:5]
    subjectfile_list = Subjectfile.objects.order_by('-update_time')[:5]
    discuss_list = Discuss.objects.order_by('-update_time')[:5]
    context = {'posts_list': posts_list, 'homework_list' : homework_list,
              "subjectfile_list" :subjectfile_list,
               'discuss_list':discuss_list}
    try:
        context['studentid'] = request.user.student.studentid
    except:
        return HttpResponseRedirect('/admin/')
    return render(request, 'jwxt/index.html', context)

@login_required
def single_post(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'jwxt/single_post.html', {'post': post})

@csrf_exempt
@login_required
def single_homework(request,homework_id):
    homework = get_object_or_404(Homework, pk=homework_id)
    if request.method == "POST":
        ff = FileForm(request.POST, request.FILES)
        if ff.is_valid():
            ansower = Homeworkansower(student=request.user.student,
                                      homework=homework,
                                      answerfile=request.FILES['file'])
            ansower.save()
    else:
        ff = FileForm()
    try:
        homework.homeworkansower_set.get(student=request.user.student)
    except:
        return render(request, 'jwxt/single_homework.html', {'homework': homework, 'uploaded':False, 'ff':ff})
    return render(request, 'jwxt/single_homework.html', {'homework': homework, 'uploaded':True})

@login_required
def single_subjectfile(request,subjectfile_id):
    subjectfile = get_object_or_404(Subjectfile, pk=subjectfile_id)
    return render(request, 'jwxt/single_subjectfile.html', {'subjectfile': subjectfile})


# @login_required
# def homework_download(request, homework_id, filename):
    # homework = get_object_or_404(Homework)

    # def file_iterator(file_name, chunk_size=512):
        # with open(file_name) as f:
            # while True:
                # c = f.read(chunk_size)
                # if c:
                    # yield c
                # else:
                    # break

    # response = StreamingHttpResponse(file_iterator(homework.questionfile.path))
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(homework.questionfile.name)

    # return response


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username = username, password=password)

        if(user is not None and user.is_active):
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            render(request, 'jwxt/login.html')

    return render(request, 'jwxt/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username",'')
        studentid = request.POST.get("studentid",'')
        password= request.POST.get("password", '')
        password2 = request.POST.get("password2", '')
        if(password != password2):
            return HttpResponse("再次密码不相同")
        if(User.objects.filter(username=username)):
            return HttpResponse("<h1>此用户名已被使用</h1>")
        if(Student.objects.filter(studentid=studentid)):
            return HttpResponse("<h1>此学号已经被使用</h1>")
        user = User.objects.create_user(username=username,password=password)
        student = Student(user=user, studentid= studentid)
        student.save()
        return HttpResponseRedirect('/login/')
    return render(request, 'jwxt/signup.html')

# @login_required
# def downfile(request, path):
    # def file_iterator(file_name, chunk_size=512):
        # with open(file_name) as f:
            # while True:
                # c = f.read(chunk_size)
                # if c:
                    # yield c
                # else:
                    # break

    # response = StreamingHttpResponse(file_iterator(path))
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(homework.questionfile.name)

    # return response
    # return HttpResponse(path)

@login_required
def single_discuss(request,discuss_id):
    discuss = get_object_or_404(Discuss, pk=discuss_id)
    if request.method == "POST":
        description = request.POST.get("description", "")
        replay = Discussreplay(discuss=discuss,
                               student=request.user.student,
                               description=description)
        replay.save()
        return HttpResponseRedirect('/discuss/' + str(discuss_id))
    replay_list = discuss.discussreplay_set.order_by('update_time')
    return render(request, 'jwxt/single_discuss.html', {'discuss': discuss, 'replay_list':replay_list})


@login_required
def new_discuss(request):
    if request.method == 'POST':
        title = request.POST.get("title",'')
        description = request.POST.get("description",'')
        discuss = Discuss(student=request.user.student,
                          title=title,
                          description=description)
        discuss.save()
        return HttpResponseRedirect('/discuss/' + str(discuss.id))
    return render(request, 'jwxt/new_discuss.html')

def test(request):
    return render(request, 'jwxt/test.html')

@login_required
def all_list(request,class_name,des_word, addres):
    the_list = class_name.objects.order_by('-update_time')
    context = {'the_list': the_list,'des_word':des_word,
               'addres':addres}
    return render(request, 'jwxt/all_list.html', context)
