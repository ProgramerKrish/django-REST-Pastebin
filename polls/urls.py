from django.urls import path
from . import views

urlpatterns = [
    # This maps the root of 'polls/' to your index view
    path('api/questions/', views.index),
    path("api/<int:question_id>",views.detail),
    path("questions/<int:question_id>/vote/",views.vote,name="vote"),
    path("questions/<int:question_id>/vote-page/",views.vote_page),
]
