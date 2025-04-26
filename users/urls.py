from django.contrib.auth import views as auth_views
from django.urls import path

from .views import SignUp
from .views import home

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/signup/', SignUp.as_view(), name='signup'),
]
