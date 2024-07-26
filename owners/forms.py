from django.forms import models

from . models import Owner

class OwnerForm(models.ModelForm):
    class Meta:
        model = Owner
        fields = ['firstname', 'lastname', 'email', 'phone', 'address']