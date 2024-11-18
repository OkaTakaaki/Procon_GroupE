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
    path('Number/', views.Number, name='Number'),
    path('reserve/', views.reserve, name='reserve'),
    path('reserve_success',views.reserveSuccess,name='reserve_success')
    # path('kari/', views.kari, name='kari'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)