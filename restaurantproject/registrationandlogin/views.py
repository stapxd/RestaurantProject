from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from django.contrib import messages

# Create your views here.
def loginUser(request):
    title = 'Логін'
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Виникла помилка, перевірте введені дані.'))
            return redirect('login')

    else:
        return render(request, 'registrationandlogin/login.html', locals())


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    title = 'Реєстрація'
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(form.cleaned_data['email'])
            print(form.cleaned_data['username'])
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = RegisterUserForm()

    return render(request, 'registrationandlogin/registration.html', locals())
