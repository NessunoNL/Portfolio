from django.shortcuts import render
from django.http import HttpResponse
from .scripts import Person

jacco = Person('Jacco')
marjolein = Person('Marjolein')

# Create your views here.
def home(request):

    context = {
        'title': 'home',
        'expenses_jacco': jacco.get_total_expenses(),
        'income_jacco': jacco.get_total_income(),
        'difference_jacco': jacco.get_difference(),
        'expenses_marjolein': marjolein.get_total_expenses(),
        'income_marjolein': marjolein.get_total_income(),
        'difference_marjolein': marjolein.get_difference(),
        'monthly_jacco': jacco.get_monthly(),
        'monthly_marjolein': marjolein.get_monthly(),
        }

    return render(request, 'budget/home.html', context)

def Jacco(request):

    colors = ['#09609e', '#0076b3', '#008dc5', '#00a4d3', '#00bbdf', '#00d2e6',
    '#00e9eb', '#47ffee']

    context = {
        'title': jacco.name,
        'expenses': jacco.get_expenses(),
        'income': jacco.get_income(),
        'total_expenses': jacco.get_total_expenses(),
        'total_income': jacco.get_total_income(),
        'total_difference': jacco.get_difference(),
        'graph_1': jacco.get_graphs(colors)[0],
        'graph_2': jacco.get_graphs(colors)[1],
        'color': '#09609e'
        }

    return render(request, 'budget/person.html', context)

def Marjolein(request):

    colors = ['#9e3f80','#a55194','#ab63a8','#b075bb','#b586cd','#ba97de',
    '#bfa9ef','#c4baff']

    context = {
        'title': marjolein.name,
        'expenses': marjolein.get_expenses(),
        'income': marjolein.get_income(),
        'total_expenses': marjolein.get_total_expenses(),
        'total_income': marjolein.get_total_income(),
        'total_difference': marjolein.get_difference(),
        'graph_1': marjolein.get_graphs(colors)[0],
        'graph_2': marjolein.get_graphs(colors)[1],
        'color': '#9e3f80'
        }
    return render(request, 'budget/person.html', context)

def changes(request):
    return render(request, 'budget/changes.html', {'title': 'changes'})
