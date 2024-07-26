from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

from .models import Customer
from .forms import CustomerForm

User = get_user_model()

# Create your views here.

@login_required(login_url='login_user')
def index(request):
    if not request.user.is_superuser: 
        return redirect('dashboard')
    else:
        customers = Customer.objects.all()
        context = {
            'customers': customers
        }
        return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        job = request.POST['job']
        date_of_birth = request.POST['date_of_birth']
        username = request.POST['username']

        default_password = 'password'

        account = User.objects.create_user(username=username, email=email, password=default_password)

        if account is not None:
            account.first_name = firstname
            account.last_name = lastname
            account.is_customer = True
            account.save()

            customer = Customer.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                job=job,
                date_of_birth=date_of_birth,
                account=account
            )

            if customer is not None:
                customer.save()
                return redirect('customers')
            else: 
                print("Error creating customer")
                account.delete()
                return render(request, 'customers/create.html')
        else: 
            print("Error creating user")
            return render(request, 'customers/create.html')
    else: 

        return render(request, 'customers/create.html')
    

def update(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
        else: 
            context = {
                'customer': customer
            }
            return render(request, 'customers/update.html', context)
    else:
        context = {
            'customer': customer
        }
        return render(request, 'customers/update.html', context)
