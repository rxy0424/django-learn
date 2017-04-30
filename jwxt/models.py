from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content_text = models.TextField()
    create_time = models.DateTimeField('创建时间',default = timezone.now, editable=False)
    update_time = models.DateTimeField('修改时间', auto_now = True)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,editable=False)
    studentid = models.IntegerField()

    def __str__(self):
        return self.user.username

class Homework(models.Model):
    title = models.CharField(max_length=200, default="homework")
    update_time = models.DateTimeField("上传时间", default = timezone.now,editable=False)
    description = models.TextField()
    questionfile = models.FileField("File",upload_to='./')

    def __str__(self):
        return self.title


class Homeworkansower(models.Model):
    student = models.ForeignKey(Student,editable=False)
    homework = models.ForeignKey(Homework,editable=False)
    update_time = models.DateTimeField("上传时间", default = timezone.now,editable=False)
    answerfile = models.FileField("File", upload_to='./')

    def fileLink(self):
        if self.questionfile:
            return '<a href="' + str(self.answerfile.url) +'">ss</a>'
        else:
            return '<a href=""></a>'
    fileLink.allow_tags=True
    fileLink.short_description= "File Link"

    def __str__(self):
        return self.homework.title

class Subjectfile(models.Model):
    title = models.CharField(max_length=200, default="Subjectfile")
    update_time = models.DateTimeField("上传时间", default = timezone.now,editable=False)
    description = models.TextField()
    realfile = models.FileField("File",upload_to='./')

    def __str__(self):
        return self.title

class Discuss(models.Model):
    student = models.ForeignKey(Student,editable=False)
    title = models.CharField(max_length=200, default="Subjectfile")
    update_time = models.DateTimeField("上传时间", default = timezone.now,editable=False)
    description = models.TextField()

    def __str__(self):
        return self.title

class Discussreplay(models.Model):
    discuss = models.ForeignKey(Discuss,editable=False)
    student = models.ForeignKey(Student,editable=False)
    update_time = models.DateTimeField("上传时间", default = timezone.now,editable=False)
    description = models.TextField()

class Multiplechoice(models.Model):
    description = models.TextField()
    choicea = models.CharField(max_length=200)
    choiceb = models.CharField(max_length=200)
    choicec = models.CharField(max_length=200)
    choiced = models.CharField(max_length=200)
    result = models.IntegerField(default=1)

class Trueorfalse(models.Model):
    description = models.TextField()
    result = models.BooleanField()

class Fillintheblank(models.Model):
    descriptiona = models.TextField()
    ansowera = models.CharField(max_length=200)
    ansowerb = models.CharField(max_length=200, null=True)
    ansowerc = models.CharField(max_length=200, null=True)
    descriptionb = models.TextField()
