from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
# Create your views here.
def index(request):
    questions=Question.objects.all()

    data={
        "quetions":[{
            "id":q.id,
            "question_text":q.question_text,
            "pub_date":q.pub_date,
        }
        ]
        for q in questions
    }

    return JsonResponse(data)

def detail(request,question_id):
    question=Question.objects.get(id=question_id)

    data={
        "id":question.id,
        "question_text":question.question_text,
        "choices":[
            {
                "id":c.id,
                "choice_text":c.choice_text,
                "votes":c.vote,
            }
            for c in question.choice_set.all()
        ]
    }

    return JsonResponse(data)