from django.conf.urls import url
from .import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

app_name ='Blogs'
urlpatterns= [
    path('',views.main_page,name='main_page'),
    path('user/<user_name>',views.user_page,name='user_page'),
    path('login/',auth_views.login, name='login'),
    path('logout/',auth_views.logout,{'next_page': '../'}, name='logout'),

]