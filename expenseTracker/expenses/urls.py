from django.urls import path

from . import views

app_name = 'expenses'
urlpatterns = [
    path('', views.index, name='index'),  # The 'index' view
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]