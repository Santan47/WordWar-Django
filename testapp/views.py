from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.models import User, Group, auth
from django.contrib import messages
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
    contents = tb_content.objects.all()
    return render(request, "index.html", {"contents": contents})

def getActiveData(request):
    contentId = request.GET["s_no"]
    content = tb_content.objects.raw('SELECT * FROM testapp_tb_content WHERE s_no = contentId')
    return JsonResponse({'data': content},safe = False)

def register(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        
        if password == confirmPassword:
            if User.objects.filter(email =email).exists():
                messages.info(request,"user already exist")
                return redirect('/register')
            else:
                user = User.objects.create_user(username = username, password=password, email= email,first_name = first_name,last_name= last_name)
                user.save();
                messages.info(request,"user created successfully.")
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"User password is not same.")
            return redirect('/register')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            contents = tb_content.objects.all()
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")
