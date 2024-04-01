from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import SignUp, LoginForm
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.
User = get_user_model()


def signup(request):
    signupform = SignUp()

    if request.method == "POST" and len(request.POST) > 0:
        rep = request.POST
        username = rep.get("username")
        first_name = rep.get("first_name")
        last_name = rep.get("last_name")
        email = rep.get("email")
        password = rep.get("password")
        city = rep.get("city")
        phone_number = rep.get("phone_number")
        location = rep.get("location")

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                   password=password, phone_number=phone_number, city=city, location=location)
        login(request, user)
        return redirect("accueil")
        pass
    return render(request, 'user_account/signup.html', {"Form": signupform})
    pass


def index(request):
    return render(request, 'store/index.html')
    pass


def logout_user(request):
    logout(request)
    return redirect("accueil")
    pass


def login_user(request):
    login_form = LoginForm()
    if request.method == "POST" and len(request.POST) > 0:
        rep = request.POST
        username = rep.get("username")
        password = rep.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("accueil")
            pass
        else:
            print(user)
            pass
        pass
    return render(request, "user_account/login.html", {"Form": login_form})
    pass

