from django.urls import path

from . import views

app_name = 'expenses'
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_expense, name="add_expense"),
    path("edit/<int:id>", views.edit_expense, name="edit_expense"),
    path("delete/<int:id>", views.delete_expense, name="delete_expense"),

]