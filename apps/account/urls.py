from django.urls import path
from account import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    # /account/user_id
    path('<user_id>', views.info)
]