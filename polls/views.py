
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F

def index(request):
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[1:6]
    template = loader.get_template('polls/index.html')
    context={'latest_question_list' : latest_question_list}
    return HttpResponse(template.render(context, request))
    '''
    latest_question_list=Question.objects.order_by('-pub_date')[1:6]
    context={'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 파이썬에서는 괄호가 있는 튜플로 여러 개의 예외 지정 가능함.
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})

    else:
        selected_choice.votes = F('votes') + 1
        # selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


