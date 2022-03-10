from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
# registration logic start
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email,
                                                password=password1)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')
# registration end


# login start
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
# login end


# logout start
def logout(request):
    auth.logout(request)
    return redirect('/')
# logout end