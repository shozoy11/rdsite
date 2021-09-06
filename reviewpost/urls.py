from django.urls import path
from .views import signupview, loginview, logoutview, indexview
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', loginview, name='login'),
    path('signup/', signupview, name='signup'),
    path('logout/', logoutview, name='logout'),
    # path("index/", login_required(indexview), name="index"),
    # path("index/", indexview.as_view(), name="index"),
    path('index/', indexview, name='index')
]
