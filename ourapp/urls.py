from django.urls import path
from . import views
from django.conf.urls import url

app_name='ourapp'

urlpatterns=[
    path('',views.login,name='index'),
]
