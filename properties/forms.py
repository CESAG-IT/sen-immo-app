from django.forms import models

from .models import Property

class PropertyOwnerForm(models.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'property_type', 'address', 'price', 'photo', 'bathrooms', 'rooms']



class PropertyAdminForm(models.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'property_type', 'address', 'price', 'photo', 'bathrooms', 'rooms', 'owner']