from django.urls import path
from . import views

app_name = 'reception_system'

urlpatterns = [
    path('index/', views.index, name="index"),
]