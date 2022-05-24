from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsurvey/', views.newsurvey, name='newsurvey'),
    path('survey/<int:para>', views.joinsurvey, name='joinsurvey'),
    path('surveyresult/<int:para>', views.surveyresult, name='surveyresult'),
    path('createuser/', views.createuser, name='createuser'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('createsurvey/', views.createsurvey, name='createsurvey'),
    path('submitsurvey/', views.submitsurvey, name='submitsurvey'),
]