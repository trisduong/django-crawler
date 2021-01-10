from django.shortcuts import render
from django.http import HttpResponse
from .models import awesome_job, fami_post, python_fami_post, sys_fami_post, com_fami_post


def index(request):
    return render(request, 'pages/home.html')


def fami(request):
    queryset = fami_post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'pages/fami.html', context)


def jobs(request):
    queryset = awesome_job.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'pages/job.html', context)


def dynamic_lookup_job_view(request, my_id):
    obj = awesome_job.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, "pages/job_detail.html", context)


def python_fami(request):
    queryset = python_fami_post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'pages/fami.html', context)


def sys_fami(request):
    queryset = sys_fami_post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'pages/fami.html', context)


def com_fami(request):
    queryset = com_fami_post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'pages/fami.html', context)
