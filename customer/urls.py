from django.urls import path

from . import views_api
from . import views_web

urlpatterns = [

    # APIs
    # Get Customers
    path('api/customers/', views_api.CustomerCreateAndList.as_view(), name='customers_list'),
    path('api/customer/<int:pk>/', views_api.CustomerDetail.as_view()),

    # Get Payment Records
    path('api/payment_records/', views_api.PaymentRecordCreateAndList.as_view(), name='payment_records_list'),
    path('api/payment_record/<int:pk>/', views_api.PaymentRecordDetail.as_view()),

    # Get Bins
    path('api/bins/', views_api.BinCreateAndList.as_view(), name='bins_list'),
    path('api/bin/<int:pk>/', views_api.BinDetail.as_view()),

    # Web
    path('dashboard/', views_web.dashboard, name='dashboard'),
    path('customers/', views_web.customers, name='customers'),
    path('payment-record/', views_web.payment_records, name='payment_records'),
    path('bins/', views_web.bins, name='bins'),
    path('employees/', views_web.employees, name='employees'),
    path('map/', views_web.maps, name='map'),
]
