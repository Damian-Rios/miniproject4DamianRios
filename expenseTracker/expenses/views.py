from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Expense


def index(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {'expenses': expenses}
    return render(request, "expenses/index.html", context)

def add_expense(request):
    return HttpResponse("Hello, world. You're adding an expense.")

def edit_expense(request):
    return HttpResponse("Hello, world. You're editing an expense.")

def delete_expense(request):
    return HttpResponse("Hello, world. You're deleting an expense.")