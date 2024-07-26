from django.forms import models

from .models import Customer

class CustomerForm(models.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'phone', 'job', 'date_of_birth']