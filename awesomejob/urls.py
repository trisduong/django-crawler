from django.urls import path
from . import views
from .views import dynamic_lookup_job_view


urlpatterns = [
    path('', views.index),
    path('familug/', views.fami),
    path('awesomejob/', views.jobs),
    path('awesomejob/<int:my_id>/', dynamic_lookup_job_view, name='awesome job'),
]
