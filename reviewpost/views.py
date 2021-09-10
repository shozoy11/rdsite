from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import ReviewModel
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

def signupview(request):
    print(request.method)
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
            db = ReviewModel.objects.create(user=username_data, bet=5000)
            user.save()
            db.save()            
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        print(User.objects.all())
    return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            object = ReviewModel.objects.filter(user=username_data).values()
            return render(request, 'index.html', {'object':object})
        else:
            print('リダイレクト')
            return redirect('login')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')    

def indexview(request):
    object_list = ReviewModel.objects.filter(user='tanaka').values()
    return render(request, 'index.html', {'object_list': object_list})
