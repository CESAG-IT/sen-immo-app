from django.shortcuts import redirect, render
from .models import Property
from owners.models import Owner
from django.contrib import messages

from .forms import PropertyAdminForm, PropertyOwnerForm

from core.utils import send_my_email

# Create your views here.

def index(request):

    if request.user.is_customer:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('dashboard')
    
    properties = None

    if request.user.is_superuser:
        properties = Property.objects.all()
    else:
        current_owner = Owner.objects.get(account=request.user)

        properties = Property.objects.filter(owner=current_owner) 
        # SELECT * FROM properties WHERE owner = request.user
    
    context = {
            'properties': properties
        }
    return render(request, 'properties/index.html', context)
    

    

def create(request):

    if request.user.is_customer:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('dashboard')
    
    form = None

    if request.method == 'POST':

        if request.user.is_superuser:
            form = PropertyAdminForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'The property has been created successfully.')
                return redirect('properties')
            else: 
                messages.error(request, 'The property could not be created.')
                return render(request, 'properties/create.html', {'form': form})
        else:
            form = PropertyOwnerForm(request.POST, request.FILES)
            current_owner = Owner.objects.get(account=request.user)
            
            if form.is_valid():
                new_property = form.save(commit=False)
                new_property.owner = current_owner
                new_property.save()

                send_my_email(request.user.email, request.user.last_name)

                if new_property is not None:
                    print("Property created")

                    messages.success(request, 'The property has been created successfully.')
                    return redirect('properties')
                else: 
                    messages.error(request, 'The property could not be created. ')
                    return render(request, 'properties/create.html', {'form': form})
            else: 
                messages.error(request, 'The property could not be created, form is invalid')
                return render(request, 'properties/create.html', {'form': form})

            # if form.is_valid():
            #     property = Property.objects.create(
            #         name = request.POST['name'],
            #         description = request.POST['description'],
            #         property_type = request.POST['property_type'],
            #         address = request.POST['address'],
            #         price = request.POST['price'],
            #         owner = current_owner,
            #         bathrooms = request.POST['bathrooms'],
            #         rooms = request.POST['rooms']
            #     )

            #     if property is not None:
            #         print("Property created")
                
            #         messages.success(request, 'The property has been created successfully.')
            #         return redirect('properties')
            #     else:
            #         messages.error(request, 'The property could not be created.')
            #         return render(request, 'properties/create.html', {'form': form})
            # else:
            #     messages.error(request, 'The property could not be created.')
            #     return render(request, 'properties/create.html', {'form': form})
    else: 
        
        if request.user.is_superuser:
            form = PropertyAdminForm()
        else: 
            form = PropertyOwnerForm()
        
        context = {
            'form': form
        }
        return render(request, 'properties/create.html', context)

def update(request, id):
    return render(request, 'properties/update.html')

def delete(request, id):
    return render(request, 'properties/delete.html')
