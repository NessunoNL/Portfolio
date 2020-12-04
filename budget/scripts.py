from .models import Incomes, Expenses, Changes
from matplotlib import pyplot as plt
from datetime import date
import numpy as np
import io
import urllib, base64

class Person:
    def __init__(self, name):
        self.name = name

    def get_income(self):
        income = Incomes.objects.filter(person=self.name)
        return income

    def get_total_income(self):
        total_income = 0
        income = Incomes.objects.filter(person=self.name)
        for _obj in income:
            total_income += _obj.amount
        return total_income

    def get_expenses(self):
        catdict = {}
        totallst = []
        for _obj in Expenses.objects.filter(person__in=[self.name, 'Joint']):
            _cat = _obj.category
            catdict[_cat] = Expenses.objects.filter(person__in=[self.name, 'Joint'], category=_cat)
        return catdict

    def get_total_expenses(self):
        total_expenses = 0
        catdict = self.get_expenses()
        for value in catdict.values():
            for obj in value:
                if obj.person == 'Joint':
                    obj.amount = obj.amount / 2
                total_expenses += obj.amount
        return total_expenses

    def get_difference(self):
        difference = self.get_total_income() - self.get_total_expenses()
        return difference

    def get_monthly(self):
        monthly = 0
        for _obj in Expenses.objects.filter(person__in=[self.name, 'Joint'], jointbankaccount=True):
            if _obj.person == "Joint":
                monthly += (_obj.amount / 2)
            else:
                monthly += _obj.amount
        return monthly

    def get_graphs(self, colors):
        plt.style.use("fivethirtyeight")

        #Graph 1: Income VS Expense
        x1_axis = [f'Inkomen \n€ {self.get_total_income()}', f'Uitgaven \n€ {self.get_total_expenses()}']
        y1_axis = [self.get_total_income(), self.get_total_expenses()]
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
        colors2 = colors.copy()
        colors2.reverse()
        x2_axis = []
        y2_axis = []
        for key, value in self.get_expenses().items():
            cat_sum = 0
            for _obj in value:
                if _obj.person == 'Joint':
                    cat_sum += (_obj.amount / 2)
                else:
                    cat_sum += _obj.amount
            y2_axis.append(cat_sum)
            fstr = f'{key} \n € {cat_sum}'
            x2_axis.append(fstr)

        y2_axis, x2_axis = zip(*sorted(zip(y2_axis, x2_axis)))

        # Create figure & axis 2
        fig2, ax2 = plt.subplots()
        ax2.barh(x2_axis, y2_axis, color=colors2, linewidth=0.5, edgecolor='black')
        x = ax2.axes.get_xaxis()
        x.set_visible(False)
        plt.tight_layout()

        # Create PNG 2
        buf2 = io.BytesIO()
        fig2.savefig(buf2, format='png')
        buf2.seek(0)
        string2 = base64.b64encode(buf2.read())
        graph_cat = urllib.parse.quote(string2)

        # Return 2 graphs as list
        return [graph_budget, graph_cat]

def get_pending_changes():
    # Check if change planned for current date or before
    all_changes = Changes.objects.all()
    pending_changes = []
    for change_obj in all_changes:
        if not change_obj.completed == True:
            pending_changes.append(change_obj)
    return pending_changes

def process_changes():
    #process eligible changes
    all_changes = Changes.objects.all()
    to_be_processed = []
    for change_obj in all_changes:
        if change_obj.date <= date.today():
            # process change
            change_obj.name.amount = change_obj.new_amount
            change_obj.completed = True
            change_obj.name.save()
            change_obj.save()
