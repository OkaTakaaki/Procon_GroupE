from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reception_system'

urlpatterns = [
    path('', views.index, name="index"),
    path('receptionNumber/', views.receptionNumber, name='receptionNumber'),
    path('complate/', views.complate, name='reception_complate'),
    path('seatsview/',views.seatsview,name='seatsview'),
    path('reserve/', views.reserve, name='reserve'),
    path('calculate_wait_time/', views.calculate_wait_time, name='calculate_wait_time'),
    path('customerCall/',views.customerCall,name='customerCall'),
    path('reserve_success',views.reserveSuccess,name='reserve_success')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)