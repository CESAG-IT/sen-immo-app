from django.shortcuts import render, redirect

from .models import Owner
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.

from .forms import OwnerForm

Account = get_user_model()

def index(request):
    owners = Owner.objects.all()
    context = {
        'owners': owners
    }
    return render(request, 'owners/index.html', context)

def create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        username = request.POST['username']

        default_password = 'test123'

        owner_account = Account.objects.create_user(username=username, email=email, password=default_password)

        if owner_account is not None:
            owner_account.first_name = firstname
            owner_account.last_name = lastname
            owner_account.is_owner = True
            owner_account.save()

            owner = Owner.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                address=address,
                account=owner_account
            )

            if owner is not None:
                print("owner created")
                messages.success(request, 'The owner has been created successfully.')
                return redirect('owners') 
            else:
                owner_account.delete()
                print("Error creating owner")
                messages.error(request, 'Error creating owner . Please try again.')
                return render(request, 'owners/create.html')
            
        else: 
            print("Error creating user")
            messages.error(request, 'Error creating owner account. Please try again.')
            return render(request, 'owners/create.html')

    return render(request, 'owners/create.html')

def update(request, id):

    owner = Owner.objects.get(id=id)
    context = {
        'owner': owner
    }

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            messages.success(request, 'The owner has been updated successfully.')
            return redirect('owners')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return render(request, 'owners/update.html', context)
    else: 
    
        return render(request, 'owners/update.html', context)
