from django.contrib.messages.storage import session
from django.shortcuts import render
from django.template import loader
from .models import Book_status, Student_Book_status, Admin, Student
from django.http import HttpResponse
from rest_framework.decorators import api_view

import library.models


# Create your views here.
@api_view(['GET'])
def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def admin_login(request):
    if request.method == "POST":
        if request.POST["username"] and request.POST["password"]:
            admin_username = request.POST["username"]
            admin_password = request.POST["password"]
            user = Student.objects.filter(email=user_username, password=user_password)
            if user:
                # session['user'] = user;
                session['email-id'] = user.email
                # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
                return redirect(url_for("home"))
            else:
                message = "Plz check username and password"
                return render_template("login.html", error=message)
        else:
            message = "Plz check username and password"
            return render_template("login.html", error=message)
    return render_template("login.html")
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

@api_view(['POST'])
def user_login(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
