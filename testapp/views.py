from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testapp.serializers import UserSerializer
from .form import NameForm


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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})