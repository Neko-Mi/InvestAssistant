from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/<int:question_id>/results/', views.results, name='results'),
    path('question/', views.question, name='question'),
    path('stocks/', views.stocks, name='stocks'),
    path('recommend_date/', views.recommend_date, name='recommend_date'),
    path('user_account/', views.user_account, name='user_account')
]