from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job


def port_list(request):
    jobs = Job.objects
    return render(request, 'jobs/port_list.html', {'jobs': jobs})


def port_detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/port_detail.html', {'job': job_detail})


def index(request):
    return render(request, 'index.html')
