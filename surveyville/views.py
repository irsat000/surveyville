from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db.models import Count, F

def index(request):
    surveyposts = Survey.objects.annotate(participations=Count('question__answer__vote__user_FK_id', distinct=True), questioncount=Count('question__id', distinct=True)).order_by('-id')
    context = {}
    context['surveys'] = surveyposts

    context['today'] = date.today()
    if request.user.is_authenticated:
        context['user'] = request.user

    return render(
        request,
        'index.html',
        context
    )
    
def surveyresult(request, para):
    surveypost = Survey.objects.get(id=para)
    context = {}
    context['survey'] = surveypost
    context['today'] = date.today()
    if request.user.is_authenticated:
        context['user'] = request.user

    questions = Question.objects.filter(survey_FK_id=para).prefetch_related('answer_set__vote_set')
    # .annotate(votes=Count('answer__vote__answer_FK_id'))
    print(questions.query)
    context['questions'] = questions

    return render(
        request,
        'surveyresult.html',
        context
    )

@csrf_exempt
def joinsurvey(request, para):
    if request.user.is_authenticated:
        context = {}
        context['today'] = date.today()
        context['user'] = request.user
        context['survey'] = Survey.objects.get(id=para)

        # questions = Question.objects.filter(survey_FK_id=para).prefetch_related('answer').all()
        questions = Question.objects.filter(survey_FK_id=para).prefetch_related('answer_set').all()
        context['questions'] = questions
        
        return render(
            request,
            'survey.html',
            context
        )
    else:
        return redirect('index')
    
def newsurvey(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }
        return render(
            request,
            'newsurvey.html',
            context
        )
    else:
        return redirect('index')

@csrf_exempt
def createuser(request):
    x = request.POST['username']
    y = request.POST['password']
    z = request.POST['email']
    user = Account.objects.create_user(username=x, password=y, email=z)
    # user = Account(username=x, password=y)
    # üstteki kod hashleme yapmaz, authenticate hashli şifre aradığı için kullanıcıyı bulamaz.
    user.save()

    # Kayıt olma tamamlandıktan sonra giriş yapma işlemi
    user = authenticate(username=x, password=y)
    if user is not None:
        login(request, user)
    return redirect('index')

@csrf_exempt
def signin(request):
    x = request.POST['username']
    y = request.POST['password']
    
    user = authenticate(username=x, password=y)
    if user is not None:
        login(request, user)
        print("Success")
    else:
        print("Login failed")
    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def createsurvey(request):
    if request.user.is_authenticated:
        questionids = request.POST.getlist('questionid')
        questions = dict({})
        for questionid in questionids:
            questiontext = request.POST[questionid + '-question']
            qanswers = tuple(request.POST.getlist(questionid + '-answer'))
            questions[questionid] = {"q": questiontext, "a": qanswers}

        # Finding the expire date.
        today = datetime.today().strftime('%Y-%m-%d')
        begindate = datetime.strptime(today, "%Y-%m-%d")
        expiredate = datetime.strftime(begindate + timedelta(days=int(request.POST['expiredate'])), '%Y-%m-%d')
        
        # Here, I am updating the database
        survey = Survey.objects.create(
            s_title=request.POST['surveytitle'],
            s_text=request.POST['description'],
            create_date=today,
            expire_date=expiredate,
            user_FK=request.user
        )
        # q = question , a = answers
        for q in questions.items():
            #print(q[1]["q"])
            question = Question.objects.create(
                q_text = q[1]["q"],
                survey_FK = survey
            )
            
            getanswers = q[1]["a"]
            for a in getanswers:
                #print(a)
                answer = Answer.objects.create(
                    a_text = a,
                    question_FK = question
                )
    return redirect('index')


@csrf_exempt
def submitsurvey(request):
    if request.user.is_authenticated:
        qids = request.POST.getlist('question')
        for qid in qids:
            Vote.objects.create(
                answer_FK_id = request.POST[qid + '-answer'],
                user_FK_id = request.user.id
            )
    return redirect('index')