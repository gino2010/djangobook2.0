from django.contrib import auth
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def user_home(request):
    return render(request, 'login.html')


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/user")
    else:
        # Show an error page
        return HttpResponseRedirect("/user")


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/user")