from django.conf.urls import patterns, url
from django.contrib import auth
from . import views

urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'users/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
    url(r'^register/', 
        views.RegisterView.as_view(), 
        name='register',
        kwargs={'template_name': 'users/register.html'}
    ),
)