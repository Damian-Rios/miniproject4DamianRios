# expenses/urls.py
from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('login/', views.login_view, name='account_login'),
    path('index/', views.index, name='index'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('signup/', views.signup_view, name='account_signup'),
    path('logout/', views.logout_view, name='logout'),
]
