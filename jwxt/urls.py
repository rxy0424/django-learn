# -*- coding : utf-8 -*-
from django.conf.urls import url
from . import views
from jwxt.models import Post,Homework,Subjectfile,Discuss

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^post/$',views.all_list,{'class_name':Post,'des_word': "公告","addres":"post"} ),
    url(r'^post/(?P<post_id>[0-9]+)/', views.single_post, name='single_post'),
    url(r'^homework/$',views.all_list,{'class_name':Homework,'des_word': "作业","addres":"homework"} ),
    url(r'^homework/(?P<homework_id>[0-9]+)/$', views.single_homework, name='single_homework'),
    url(r'^subjectfile/$',views.all_list,{'class_name':Subjectfile,'des_word': "课件","addres":"subjectfile"} ),
    url(r'^subjectfile/(?P<subjectfile_id>[0-9]+)/$', views.single_subjectfile, name='single_subjectfile'),
    url(r'^discuss/$',views.all_list,{'class_name':Discuss,'des_word': "讨论","addres":"discuss"} ),
    url(r'^discuss/(?P<discuss_id>[0-9]+)/$', views.single_discuss, name='single_discuss'),
    url(r'^discuss/new/$', views.new_discuss, name='new_discuss'),
    # url(r'^homework/(?P<homework_id>[0-9]+)/(?P<filename>.*)/', views.homework_download, name='homework_download'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^logout/', views.logout, name = 'logout'),
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^test/', views.test, name= 'test'),
]
