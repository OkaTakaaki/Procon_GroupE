from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee/', views.employee, name="employee"),
    path('item/', views.item, name="employee_item"),
    path('confirm/', views.confirm, name="employee_confirm"),
    path('new_seat/', views.new_seat, name="employee_new_seat"),
    path('complate/', views.complate, name="employee_complate")
]