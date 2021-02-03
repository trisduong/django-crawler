from django.urls import path
from . import views
from .views import dynamic_lookup_job_view


urlpatterns = [
    path('', views.index),
    path('familug/new', views.fami),
    path('awesomejob/', views.jobs),
    path('awesomejob/<int:my_id>/', dynamic_lookup_job_view, name='awesome job'),
    path('familug/python', views.python_fami),
    path('familug/sysadmin', views.sys_fami),
    path('familug/command', views.com_fami),
]
