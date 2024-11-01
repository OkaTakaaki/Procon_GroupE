from django.urls import path
from . import views

app_name = 'reception_system'

urlpatterns = [
    path('', views.index, name="index"),
    path('reception/', views.reception, name='reception'),
    path('language/', views.language, name='language'),
    path('complate/', views.complate, name='reception_complate'),
]