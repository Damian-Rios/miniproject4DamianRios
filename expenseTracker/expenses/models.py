from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Utilities', 'Utilities'),
        ('Rent/Mortgage', 'Rent/Mortgage'),
        ('Debt', 'Debt'),
        ('Healthcare', 'Healthcare'),
        ('Insurance', 'Insurance'),
        ('Savings', 'Savings'),
        ('Necessities', 'Necessities'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - ${self.amount}"
