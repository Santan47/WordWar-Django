from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testapp.serializers import UserSerializer
from testapp.models import tb_content


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    
def uploadContentData(request):
    heading = request.POST["title"];
    contentData = request.POST["content"];

    uploadData = tb_content(userid = 1,Title = heading, content = contentData)
    uploadData.save();

    return HttpResponse("data saved successfully");

# Create your views here.
def index(request):
    today = datetime.now()
    contents = tb_content.objects.all()
    print(contents) 
    return render(request, "navigationBody.html", {"contents": contents})
   # return HttpResponse("heyo m here")
