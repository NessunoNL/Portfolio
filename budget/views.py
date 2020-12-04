from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Changes
from .scripts import Person, get_pending_changes, process_changes

jacco = Person('Jacco')
marjolein = Person('Marjolein')

# Create your views here.
def home(request):
    process_changes()
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
    process_changes()
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
    process_changes()
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
    context = {
        'title': 'Veranderingen',
        'pending_changes': get_pending_changes(),
    }

    return render(request, 'budget/changes.html', context)

class ChangeCreateView(SuccessMessageMixin, CreateView):
    model = Changes
    template_name = 'budget/changes_create.html'
    fields = ['name', 'new_amount', 'date']
    context_object_name = 'pending_changes'
    success_url = '../'
    success_message = "Toevoegen succesvol!"

class ChangeDeleteView(DeleteView):
    model = Changes
    template_name = 'budget/changes_delete.html'
    context_object_name = 'pending_changes'
    success_url = '../../'
    success_message = "Verwijderen succesvol!"
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(ChangeDeleteView, self).delete(request, *args, **kwargs)
