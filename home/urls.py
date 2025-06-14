from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login',views.LoginInterfaceView.as_view(),name='login'),
    path('logout',views.user_logout,name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]