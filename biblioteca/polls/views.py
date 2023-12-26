from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "lastest_question_list": lastest_question_list,
    }
    #output = ", ".join([q.question_text for q in lastest_question_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return  HttpResponse("Tu estas buscando la pregunta %s" % question_id)

def results(request, question_id):
    response = "Tu estas buscando en los resultados de preguntas  %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("tu estas votando sobre la pregunta %s ." % question_id)
