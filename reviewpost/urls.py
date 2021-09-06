from django.urls import path
from .views import signupview, loginview, logoutview, indexview
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
   path("", login_required(indexview), name="index"),
]
