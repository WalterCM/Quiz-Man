#from django.shortcuts import render
from django.shortcuts import render

from .models import Exam

def index(request):
    latest_exam_list = Exam.objects.order_by('-pub_date')[:5]
    context = {
        'latest_exam_list': latest_exam_list
    }

    return render(request, 'exams/index.html', context)

def detail(request, exam_id):
    return HttpResponse("You're looking at exam %s." % exam_id)

def results(request, exam_id):
    response = "You're looking at the results of an exam %s."
    return HttpResponse(response % exam_id)
