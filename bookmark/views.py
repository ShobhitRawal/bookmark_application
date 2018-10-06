from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Bookmark
from .forms import *


def main_page(request):
    
    Context={ 'user': request.user }
    return render(request,'bookmark/home.html',Context)

def user_page(request,user_name):
    
    try:
        user1= User.objects.get(username=user_name)
    except:
        raise Http404('Requested user not found.')
    
    bookmarks = user1.bookmark_set.all()
    Context ={
        'user_name':user_name,
        'bookmarks':bookmarks
        }

    return render(request,'bookmark/user_page.html',Context)

def register_page(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            context={'user':user}
            return render(request,'bookmark/home.html',context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request,'registration/register.html', context)



    
