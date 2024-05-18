from django.urls import path
from . import views

urlpatterns = [
    path('users_per_company/', views.users_per_company, name='users_per_company'),
    path('daily_user_growth/', views.daily_user_growth, name='daily_user_growth'),
]
