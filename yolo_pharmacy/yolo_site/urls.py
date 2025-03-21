from django.urls import path
from . import views

from .views_print import print_bill



urlpatterns = [
   path('print-bill/<int:bill_id>/', print_bill, name='print_bill'),
   path('wprint-bill/<int:pk>/', views.bill_printweb, name='bill_printweb'),

    #path('download-bill/<int:pk>/', download_bill, name='download_bill'),
  
    path('', views.IndexView.as_view(), name='index'),
    path('emp_list/', views.EmpListView.as_view(), name='emp_list'),
    path('emp_detail/<int:pk>/', views.EmpDetailView.as_view(), name='emp_detail'),
    path('emp_delete/<int:pk>/', views.EmpDeleteView.as_view(), name='emp_delete'),
    path('emp_edit/<int:pk>/', views.EmpUpdateView.as_view(), name='emp_edit'),
    path('register/', views.register, name='register'),
    path('comp_list/', views.CompListView.as_view(), name='comp_list'),
    path('comp_detail/<int:pk>/', views.CompDetailView.as_view(), name='comp_detail'),
    path('comp_delete/<int:pk>/', views.CompDeleteView.as_view(), name='comp_delete'),
    path('comp_edit/<int:pk>/', views.CompUpdateView.as_view(), name='comp_edit'),
    path('create/', views.CompCreateView.as_view(), name='comp_create'),
    path('create/med/', views.MedCreateView.as_view(), name='med_create'),
    path('med_detail/<int:pk>/', views.MedDetailView.as_view(), name='med_detail'),
    path('med_list/', views.MedListView.as_view(), name='med_list'),
    path('med_delete/<int:pk>/', views.MedDeleteView.as_view(), name='med_delete'),
    path('med_edit/<int:pk>/', views.MedUpdateView.as_view(), name='med_edit'),
    path('create/bill/', views.BillCreateView.as_view(), name='bill_create'),
    path('bill_detail/<int:pk>/', views.BillDetailView.as_view(), name='bill_detail'),
    path('bill_list/', views.BillListView.as_view(), name='bill_list'),
    path('bill_delete/<int:pk>/', views.BillDeleteView.as_view(), name='bill_delete'),
    path('about/', views.AboutView.as_view(), name='about'),
]