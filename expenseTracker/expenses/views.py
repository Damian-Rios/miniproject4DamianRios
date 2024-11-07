from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.http import JsonResponse

def index(request):
    expenses = Expense.objects.filter(user=request.user)  # Assuming you're filtering by the logged-in user
    context = {'expenses': expenses}
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    # Pass the CATEGORY_CHOICES to the template
    category_choices = Expense.CATEGORY_CHOICES

    if request.method == 'POST':
        # Get data from POST request
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')

        # Save the expense manually
        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            description=description,
            date=date
        )

        return redirect('expenses:index')  # Redirect to the home page after adding

    return render(request, 'expenses/add_expense.html', {'category_choices': category_choices})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':
        # Update fields from the form
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')
        expense.date = request.POST.get('date')

        expense.save()  # Save the updated expense
        return redirect('expenses:index')

    context = {'expense': expense}
    return render(request, 'expenses/edit_expense.html', context)

def delete_expense(request, expense_id):
    # Get the expense object to delete
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':  # Only allow deletion via POST request
        expense.delete()
        return redirect('expenses:index')  # Redirect to the expense list page

    # If the request is not POST, we might want to return an error page or redirect.
    return JsonResponse({"error": "Invalid request method."}, status=405)
