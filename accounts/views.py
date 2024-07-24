from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def register_customer(request):
    if request.method == 'POST': 
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        new_user = User.objects.create_user(username=username, email=email, password=password)

        if new_user is not None:
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.is_customer = True
            new_user.save()
            return redirect('login_user')
        else: 
            print("Error creating user")
            return render(request, 'accounts/register_customer.html')

    else: 

        return render(request, 'accounts/register_customer.html')


def register_owner(request):
    pass

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-customer')
        else:
            print("Error logging in")
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')
