from django.conf.urls import url, include
from django.urls import path, re_path
from testapp import views as myview



urlpatterns = [
    path('', myview.index,name='index'),
    path('uploadContent', myview.uploadContentData, name='uploadContentData'),
    path('register', myview.register, name='register'),
    path('login', myview.login, name='login'),
    path('logout', myview.logout, name='logout'),
    path('content/<str:card_id>', myview.getActiveData, name='getActiveData')
]