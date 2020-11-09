from django.urls import path
from . import views



urlpatterns = [
    path('paper_list', views.PapersListView.as_view(), name='paper_list'),
    path('detail/<int:pk>/', views.PapersDetailView.as_view(), name='detail'),
    path('result/<int:pk>/', views.QuestionUpdateView.as_view(), name='result'),
    path('check/<int:pk>/', views.Check_answerView.as_view(), name='check'),
    path('set_paper/', views.PapersCreateView.as_view(), name='set_paper'),
    path('set_questions/', views.QuestionCreateView.as_view(), name='set_questions'),
]
