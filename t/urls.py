from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='home'),
    # path('<pk>', views.disease_detail, name='disease_detail'),
    path('<pk>/medicines', views.disease_medicine, name='disease_medicines'),
    path('<pk>/medicines/stores/', views.store, name='store_detail')
    # path('mdedicine/<pk>', name='medicine_detail')
]
