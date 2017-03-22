from django.shortcuts import render

from exams.models import Exam

def index(request):
    latest_exam_list = Exam.objects.order_by('-pub_date')[:5]
    for exam in latest_exam_list:
        print(exam.exam_name)
    context = {
        'latest_exam_list': latest_exam_list
    }

    return render(request, './index.html', context)
