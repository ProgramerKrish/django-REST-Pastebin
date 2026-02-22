from django.shortcuts import render
from django.http import JsonResponse
from .models import Question,Choice
from django.shortcuts import get_object_or_404
import json
# Create your views here.
def index(request):
    try:
        questions=Question.objects.all()
    except Exception as e:
        return JsonResponse(
                {
                    "error":"failed to fetch Questions"},
                
                status=500
             )   
    data={
        "questions":[{
            "question_id":q.id,
            "question_text":q.question_text,
            "pub_date": q.pub_date
        }
        for q in questions
        ]
    }

    return JsonResponse(data)

def detail(request,question_id):
    question=get_object_or_404(Question,id=question_id)

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
""" def vote(request,question_id):
    question=get_object_or_404(Question,id=question_id)
    data={
        "id":question_id,
        "choices":[{"choice_id":c.id,
                    "choice_text":c.choice_text,
                    "vote":c.vote,
                    }
                    for c in question.choice_set.all()
                    ]
    }
    return JsonResponse(data) """

""" def vote(request,question_id):
    if request.method != "POST":
        return JsonResponse(
            {"error":"only POST method allowed"},
            status=405
        )
    question=get_object_or_404(Question,id=question_id)

    try:
        body=json.loads(request.body)
        choice_id=body["choice_id"]
    except(json.JSONDecodeError,KeyError):
        return JsonResponse(
            {"error":"invalid JSON or missing choice_id"},
            status=400
        )
    choice=get_object_or_404(Choice,id=choice_id,question=question)
    choice.vote+=1
    choice.save()

    return JsonResponse(
        {
            "message":"vote recoreded",
            "question_text":question.id,
            "choice_id":choice.id,
            "total_votes":choice.vote
        }
    )
 """
def vote(request,question_id):
    if request.method != "POST":
        return JsonResponse(
            {"error":"only POST method allowed"},
            status=405
        )
    question=get_object_or_404(Question,id=question_id)

    try:
        choice_id=request.POST["choice"]
    except(KeyError):
        return JsonResponse(
            {"error":"invalid JSON or missing choice_id"},
            status=400
        )
    choice=get_object_or_404(Choice,id=choice_id,question=question)
    choice.vote+=1
    choice.save()

    return JsonResponse(
        {
            "message":"vote recoreded",
            "question_text":question.question_text,
            "choice_id":choice.id,
            "total_votes":choice.vote
        }
    )

def vote_page(request,question_id):
    question=get_object_or_404(Question,id=question_id)
    return(render(request,"polls/votes_test.html",{"question":question}))