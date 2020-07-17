from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Choice, Question, Stock, Answer

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

def recommend_date(request):
    try:
        money = request.user.money
        risk = request.user.risk
        stock_list = Stock.objects.order_by('price')
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")

    money, money_val = setMoney(money)
    risk_min, risk_val = setRisk(risk)

    return render(request, 'recommend_date.html',
                  {'stock_list': stock_list,
                   'money': money,
                   'money_val': money_val,
                   'risk': risk,
                   'risk_val': risk_val,
                   'risk_min': risk_min
                   })

def user_account(request):
    return render(
        request,
        'user_account.html',
        {'username': request.user.username,
         'password': request.user.email,
         'money': request.user.money,
         'risk': request.user.risk,
         'time_invest': request.user.time_invest
         }
    )

def stocks(request):
    try:
        money = request.user.money
        risk = request.user.risk
        time_invest = request.user.time_invest
        stock_list = Stock.objects.order_by('price')
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")

    money, money_val = setMoney(money)
    risk_min, risk_val = setRisk(risk)

    return render(request, 'stock.html',
                  {'stock_list': stock_list,
                   'money': money,
                   'money_val': money_val,
                   'risk': risk,
                   'risk_val': risk_val,
                   'risk_min': risk_min,
                   'time_invest': time_invest
                   })

def question(request):
    try:
        question_list = Question.objects.order_by('id')
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'question.html', {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "Вы не выбрали ответ.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # answer = Answer()
        # answer.question = question
        # answer.user = request.user
        # answer.choice =  selected_choice
        # answer.save()
        setAnswers(request.user, question_id, selected_choice.id)
        request.user.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('main:results',
                                            args=(question.id,)))

def setMoney(money):
    if money == 'минимальный':
        money = '< 50 тыс. руб.'
        money_val = 400
    elif money == 'средний':
        money = '< 500 тыс. руб.'
        money_val = 4000
    else:
        money = '> 500 тыс. руб.'
        money_val = 99999999

    return money, money_val

def setRisk(risk):
    if risk == 'минимальный':
        risk_min = 0
        risk_val = 6
    elif risk == 'средний':
        risk_min = 6
        risk_val = 12
    else:
        risk_min = 12
        risk_val = 100
    return risk_min, risk_val

def setAnswers(user, question_id, selected_choice):
    if question_id == 1:
        if selected_choice == 1:
            answer = 'минимальный'
        elif selected_choice == 2:
            answer = 'средний'
        else:
            answer = 'высокий'
        user.money = answer

    elif question_id == 2:
        if selected_choice == 4:
            answer = 'минимальный'
        elif selected_choice == 5:
            answer = 'средний'
        else:
            answer = 'высокий'
        user.risk = answer
    else:
        if selected_choice == 7:
            answer = 3
        elif selected_choice == 8:
            answer = 6
        else:
            answer = 12
        user.time_invest = answer