from django.conf.urls import patterns, url,

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new$', views.task_create, name='task_new'),
    url(r'^edit/(?P<pk>\d+)$', views.task_update, name='task_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.task_delete, name='task_delete'),
]
