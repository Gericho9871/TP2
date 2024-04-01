from django.urls import path

from .views import *

urlpatterns = [
    path('account/login', login_user, name="login"),
    path('account/signup', signup, name="signup"),
    path('logout', logout_user, name="logout"),
]
