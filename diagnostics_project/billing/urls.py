from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('all_bills/', views.all_bills, name='all_bills'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('all_bills/', views.all_bills, name='all_bills'),
    path('all_patients/', views.all_patients, name='all_patients'),
]
