from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from models import JobPosting, Office

def job_index(request):
    jobs = JobPosting.objects.all()
    template = loader.get_template('job_index.html')
    context = {
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))


def office_index(request):
    offices = Office.objects.all()
    template = loader.get_template('office_index.html')
    context = {
        'offices': offices,
    }
    return HttpResponse(template.render(context, request))

