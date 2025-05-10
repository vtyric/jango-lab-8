from django.urls import path

from .views import SignUp, AppLogoutView, AppLoginView
from .views import home

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/login/', AppLoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('accounts/logout/', AppLogoutView.as_view(
        next_page='home'
    ), name='logout'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
]
