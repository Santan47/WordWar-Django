from django.conf.urls import url, include
from django.urls import path, re_path
from testapp import views as myview



urlpatterns = [
    path('', myview.index,name='index'),
    path('uploadContent', myview.uploadContentData, name='uploadContentData')
]