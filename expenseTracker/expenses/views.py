from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout


def index(request):
    expenses = Expense.objects.filter(user=request.user)  # Filtering expenses by the logged-in user
    context = {'expenses': expenses}
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    category_choices = Expense.CATEGORY_CHOICES  # Pass category choices to the template

    if request.method == 'POST':
        # Get data from the POST request
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')

        # Validate data
        if not amount or not category or not description or not date:
            messages.error(request, "All fields are required.")
            return redirect('expenses:add_expense')

        # Save the expense manually
        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            description=description,
            date=date
        )

        messages.success(request, "Expense added successfully.")
        return redirect('expenses:index')  # Redirect to the home page after adding

    return render(request, 'expenses/add_expense.html', {'category_choices': category_choices})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the owner of the expense
    if expense.user != request.user:
        messages.error(request, "You are not authorized to edit this expense.")
        return redirect('expenses:index')

    if request.method == 'POST':
        # Update fields from the form
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')
        expense.date = request.POST.get('date')

        expense.save()  # Save the updated expense
        messages.success(request, "Expense updated successfully.")
        return redirect('expenses:index')

    context = {'expense': expense}
    return render(request, 'expenses/edit_expense.html', context)

def delete_expense(request, expense_id):
    # Get the expense object to delete
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the owner of the expense
    if expense.user != request.user:
        return JsonResponse({"error": "You are not authorized to delete this expense."}, status=403)

    if request.method == 'POST':  # Only allow deletion via POST request
        expense.delete()
        messages.success(request, "Expense deleted successfully.")
        return redirect('expenses:index')  # Redirect to the expense list page

    # Handle non-POST requests
    return JsonResponse({"error": "Invalid request method. Use POST to delete."}, status=405)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('expenses:index')  # Redirect to home page if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('expenses:index')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'expenses/login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('expenses:index')  # Redirect to home if already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('expenses:account_login')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Please correct the error(s) below.')

    else:
        form = UserCreationForm()

    return render(request, 'expenses/signup.html', {'form': form})


def logout_view(request):
    # Log out the user
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('expenses:account_login')  # Redirect to login page after logout