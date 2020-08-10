from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic import View

def uploadContentData(request):
   print("data is here")
      # return render(request, "index.html", {"date": today})

# Create your views here.
def index(request):
   today = datetime.now().date()
   return render(request, "index.html", {"date": today})
   # return HttpResponse("heyo m here")
