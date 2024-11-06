from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    # Display key fields for quick review
    list_display = ('user', 'amount', 'category', 'description', 'date')

    # Allow filtering by user, category, and date
    list_filter = ('user', 'category', 'date')

    # Enable searching for specific expenses by category or description
    search_fields = ('category', 'description')


admin.site.register(Expense, ExpenseAdmin)
