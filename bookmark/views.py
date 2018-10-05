from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Bookmark

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


    
