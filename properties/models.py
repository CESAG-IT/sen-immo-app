from django.db import models

# Create your models here.

class Property(models.Model):
    TYPES = (
        ('vil', 'Villa'),
        ('apt', 'Appartement'),
        ('sto', 'Magasin')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=3, choices=TYPES) # type 
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="properties/", default="default.png")
    bathrooms = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()

    owner = models.ForeignKey("owners.Owner", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + " - " + self.owner.firstname

