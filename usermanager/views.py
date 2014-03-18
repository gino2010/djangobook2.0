from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/user")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

'''about user permission and group
you can get user object by auth.authenticate() fuction, use user.user_permission.add() function
to change user permission, then you can find the record in your database auth_user_user_permission table.
other way, you can create permission group by Group model, and add permission in this group and assign this group
to user by user.groups.add() function, then you can find this record in auth_user_groups table in your database.'''
