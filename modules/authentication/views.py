from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from modules.authentication.forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                msg = 'Username or Password WRONG!'
        else:
            msg = 'Error validating the form'

    return render(request, "login.html", {"form": form, "msg": msg})

