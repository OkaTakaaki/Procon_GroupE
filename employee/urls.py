from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee/', views.employee, name="employee"),
    path('item/', views.item, name="employee_item"),
    path('confirm/', views.confirm, name="employee_confirm"),
    path('register/', views.register, name="employee_register"),
]