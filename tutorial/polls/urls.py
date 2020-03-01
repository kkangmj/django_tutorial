
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
    '''
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/result/', views.result, name="result"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    '''
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='result'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]


