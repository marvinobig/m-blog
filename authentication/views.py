from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            dashboardUrl = reverse('dashboard', kwargs={'userId': user.id})

            return redirect(dashboardUrl)
        else:
            form = RegisterForm()
            context = {"form": form}

            return render(request, "register.html", context)
    else:
        form = RegisterForm(request.POST)
        context = {"form":form}
        return render(request, 'register.html', context)
        

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            dashboardUrl = reverse('dashboard', kwargs={'userId': user.id})

            return redirect(dashboardUrl)
        else:
            errMsg = "Invalid credentials"
            context = { "err": errMsg}

            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def logoutView(request):
    if request.method == "POST":
        logout(request)

        return redirect('login')
    else:
        return render(request, "logout.html")