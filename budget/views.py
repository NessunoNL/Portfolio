from django.shortcuts import render
from django.http import HttpResponse
from .models import incomes, expenses
from matplotlib import pyplot as plt
from django.db.models import Sum
import numpy as np
import io
import urllib, base64

# Create your views here.
def home(request):
    # Context
    # Income
    total_income_jacco = 0
    total_income_marjolein = 0
    income_jacco = incomes.objects.filter(person='Jacco')
    income_marjolein = incomes.objects.filter(person='Marjolein')
    for _obj in income_jacco:
        total_income_jacco += _obj.amount
    for _obj in income_marjolein:
        total_income_marjolein += _obj.amount

    #Expenses
    total_expenses_jacco = 0
    total_expenses_marjolein = 0
    for _obj in expenses.objects.filter(person__in=['Jacco', 'Joint']):
        if _obj.person == "Joint":
            total_expenses_jacco += (_obj.amount / 2)
        else:
            total_expenses_jacco += _obj.amount
    for _obj in expenses.objects.filter(person__in=['Marjolein', 'Joint']):
        if _obj.person == "Joint":
            total_expenses_marjolein += (_obj.amount / 2)
        else:
            total_expenses_marjolein += _obj.amount

    # Monthly
    monthly_jacco = 0
    monthly_marjolein = 0
    for _obj in expenses.objects.filter(person__in=['Jacco', 'Joint'], jointbankaccount=True):
        if _obj.person == "Joint":
            monthly_jacco += (_obj.amount / 2)
        else:
            monthly_jacco += _obj.amount

    for _obj in expenses.objects.filter(person__in=['Marjolein', 'Joint'], jointbankaccount=True):
        if _obj.person == "Joint":
            monthly_marjolein += (_obj.amount / 2)
        else:
            monthly_marjolein += _obj.amount

    context = {
        'title': 'home',
        'expenses_jacco': total_expenses_jacco,
        'income_jacco': total_income_jacco,
        'difference_jacco': total_income_jacco - total_expenses_jacco,
        'expenses_marjolein': total_expenses_marjolein,
        'income_marjolein': total_income_marjolein,
        'difference_marjolein': total_income_marjolein - total_expenses_marjolein,
        'monthly_jacco': monthly_jacco,
        'monthly_marjolein': monthly_marjolein,
        }

    return render(request, 'budget/home.html', context)

def Jacco(request):
    # Context for page Jacco
    # Expenses

    catdict = {}
    total_expenses = 0
    totallst = []
    for _obj in expenses.objects.filter(person__in=['Jacco', 'Joint']):
        _cat = _obj.category
        catdict[_cat] = expenses.objects.filter(person__in=['Jacco', 'Joint'], category=_cat)
    for value in catdict.values():
        for obj in value:
            if obj.person == 'Joint':
                obj.amount = obj.amount / 2
            total_expenses += obj.amount

    # Income
    total_income = 0
    income = incomes.objects.filter(person='Jacco')
    for _obj in income:
        total_income += _obj.amount

    #Graphs
    colors = ['#09609e', '#0076b3', '#008dc5', '#00a4d3', '#00bbdf', '#00d2e6',
    '#00e9eb', '#47ffee']
    plt.style.use("fivethirtyeight")

    #Graph 1: Income VS Expense
    x1_axis = ['Inkomen \n' + '€ ' + str(total_income) , 'Uitgaven \n' + '€ ' + str(total_expenses)]
    y1_axis = [total_income, total_expenses]
    # Create figure & axis
    fig1, ax1 = plt.subplots()
    ax1.bar(x1_axis, y1_axis, color=colors, label='Budget', linewidth=0.5, edgecolor='black') # Plot bars
    y = ax1.axes.get_yaxis()
    y.set_visible(False)
    plt.tight_layout()
    #Create PNG
    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    graph_budget = urllib.parse.quote(string)

    #Graph 2: Expense per category
    colors.reverse()
    x2_axis = []
    y2_axis = []
    for key, value in catdict.items():
        cat_sum = 0
        for _obj in value:
            cat_sum += _obj.amount
        y2_axis.append(cat_sum)
        fstr = f'{key} \n € {cat_sum}'
        x2_axis.append(fstr)

    y2_axis, x2_axis = zip(*sorted(zip(y2_axis, x2_axis)))

    # Create figure & axis 2
    fig2, ax2 = plt.subplots()
    ax2.barh(x2_axis, y2_axis, color=colors, linewidth=0.5, edgecolor='black')
    x = ax2.axes.get_xaxis()
    x.set_visible(False)
    plt.tight_layout()

    # Create PNG 2
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    graph_cat = urllib.parse.quote(string2)

    context = {
        'title': 'Jacco',
        'expenses': catdict,
        'income': income,
        'total_expenses': total_expenses,
        'total_income': total_income,
        'total_difference': total_income - total_expenses,
        'graph_1': graph_budget,
        'graph_2': graph_cat,
        'color': '#09609e'
        }

    return render(request, 'budget/person.html', context)

def Marjolein(request):

    # Context for page Marjolein
    # Expenses
    catdict = {}
    total_expenses = 0
    for _obj in expenses.objects.filter(person__in=['Marjolein', 'Joint']):
        _cat = _obj.category
        catdict[_cat] = expenses.objects.filter(person__in=['Marjolein', 'Joint'], category=_cat)
    for value in catdict.values():
        for obj in value:
            if obj.person == 'Joint':
                obj.amount = obj.amount / 2
            total_expenses += obj.amount

    # Income
    total_income = 0
    income = incomes.objects.filter(person='Marjolein')
    for _obj in income:
        total_income += _obj.amount

    #Graphs
    plt.style.use("seaborn-deep")
    colors = ['#9e3f80','#a55194','#ab63a8','#b075bb','#b586cd','#ba97de',
    '#bfa9ef','#c4baff']
    #Graph 1: Income VS Expense
    x1_axis = ['Inkomen \n' + '€ ' + str(total_income) , 'Uitgaven \n' + '€ ' + str(total_expenses)]
    y1_axis = [total_income, total_expenses]
    # Create figure & axis
    fig1, ax1 = plt.subplots()
    ax1.bar(x1_axis, y1_axis, color=colors, label='Budget', linewidth=0.5, edgecolor='black') # Plot bars
    xlabel = y1_axis # Label bars
    y = ax1.axes.get_yaxis()
    y.set_visible(False)
    plt.tight_layout()
    #Create PNG
    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    graph_budget = urllib.parse.quote(string)

    #Graph 2: Expense per category
    colors.reverse()
    x2_axis = []
    y2_axis = []
    for key, value in catdict.items():
        cat_sum = 0
        for _obj in value:
            cat_sum += _obj.amount
        y2_axis.append(cat_sum)
        fstr = f'{key} \n € {cat_sum}'
        x2_axis.append(fstr)

    y2_axis, x2_axis = zip(*sorted(zip(y2_axis, x2_axis)))

    # Create figure & axis 2


    fig2, ax2 = plt.subplots()
    ax2.barh(x2_axis, y2_axis, color=colors, linewidth=0.5, edgecolor='black')
    x = ax2.axes.get_xaxis()
    x.set_visible(False)
    plt.tight_layout()

    # Create PNG 2
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    graph_cat = urllib.parse.quote(string2)

    context = {
        'title': 'Marjolein',
        'expenses': catdict,
        'income': income,
        'total_expenses': total_expenses,
        'total_income': total_income,
        'total_difference': total_income - total_expenses,
        'graph_1': graph_budget,
        'graph_2': graph_cat,
        'color': '#9e3f80'
        }
    return render(request, 'budget/person.html', context)

def changes(request):
    return render(request, 'budget/changes.html', {'title': 'changes'})
