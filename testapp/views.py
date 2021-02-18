from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testapp.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    
def uploadContentData(request):
      print(request.POST) 

# Create your views here.
def index(request):
    today = datetime.now()
    print(request) 
    return render(request, "navigationBody.html", {"time": today})
   # return HttpResponse("heyo m here")