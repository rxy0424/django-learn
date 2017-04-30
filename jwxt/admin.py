from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db import models

from jwxt.models import Student,Post, Homework,Homeworkansower,Subjectfile,Discuss,Discussreplay
from jwxt.models import Multiplechoice,Trueorfalse,Fillintheblank

admin.site.register(Multiplechoice)
admin.site.register(Trueorfalse)
admin.site.register(Fillintheblank)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time', 'update_time', )
    fielsds = ('title', 'create_time', 'update_time' ,'content_text')

admin.site.register(Post, PostAdmin)

class SubjectfileAdmin(admin.ModelAdmin):
    readonly_fields= ('update_time', )

admin.site.register(Subjectfile, SubjectfileAdmin)

class StudentInline(admin.StackedInline):
    model = Student
    verbose_name_plural = 'student'

class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ReplayInline(admin.TabularInline):
    model = Discussreplay
    readonly_fields = ('student', 'update_time', )
    fields = ('student', 'description', 'update_time')
    extra = 0

class DiscussAdmin(admin.ModelAdmin):
    readonly_fields = ('student', 'update_time', )
    fields = ('title', 'student' , 'update_time', 'description')
    inlines = (ReplayInline,)

admin.site.register(Discuss, DiscussAdmin)

class HomeworkansowerInline(admin.TabularInline):
    readonly_fields = ('student', 'update_time', )
    fields = ('student', 'answerfile', 'update_time')
    model = Homeworkansower
    extra = 0

class HomeworkAdmin(admin.ModelAdmin):
    readonly_fields = ('update_time', )
    inlines = (HomeworkansowerInline,)
    # formfield_overrides = {
        # models.FileField :{'widget':None},
    # }
    # list_display = ('questionfile',)
admin.site.register(Homework, HomeworkAdmin)
