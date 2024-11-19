from django.urls import path
from . import views

app_name = 'reception_system'

urlpatterns = [
    path('', views.index, name="index"),
    path('select_num_people/', views.select_num_people, name='select_num_people'),
    path('language/', views.language, name='language'),
    path('complate/', views.complate, name='reception_complate'),
]