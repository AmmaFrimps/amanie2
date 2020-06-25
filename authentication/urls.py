from django.urls import path

from . import views_api, views_web

urlpatterns = [

    # APIs
    path('api/', views_api.api_root),

    # Signup
    path('api/register/', views_api.CreateUserAPIView.as_view(), name='api_register'),

    # Login
    path('api/login/obtain_token/', views_api.authenticate_user, name='obtain_token'),

    # Get Users
    path('api/users/', views_api.UserList.as_view(), name='users_list'),
    path('api/users/<int:pk>/', views_api.UserDetail.as_view()),

    # Web
    path('', views_web.index, name='index'),
    path('login', views_web.user_login, name='login'),
    path('forgot-password', views_web.forgot_password, name='forgot_password'),
    path('logout', views_web.user_logout, name='logout'),
    path('register', views_web.register, name='register'),

]
