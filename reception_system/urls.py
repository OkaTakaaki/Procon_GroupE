from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reception_system'

urlpatterns = [
    path('', views.index, name="index"),
    path('reception/', views.reception, name='reception'),
    path('language/', views.language, name='language'),
    path('complate/', views.complate, name='reception_complate'),
<<<<<<< HEAD
    path('reserve/', views.reserve, name='reserve')
=======
    path('kari/', views.kari, name='kari'),
>>>>>>> 04b5717fbb3da5c71457620e6c74b2256df21b46
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)