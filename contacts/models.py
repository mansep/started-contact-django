from django.db import models
from app.models import Country

# Create your models here.

class Contact(models.Model):
    """
        contacts model 
    """

    TYPE_CONTACT = (
        ('C', 'Client'),
        ('P', 'Provider'),
        ('E', 'Employee'),
    )

    id_document = models.CharField(max_length=50) #Chile RUT/RUN, Perú RUC/DNI, España, Argentina DNI, México RFC/CURP https://es.wikipedia.org/wiki/Documento_de_identidad
    name = models.CharField(max_length=60, blank=False, null=False)
    type = models.CharField(max_length=1, choices=TYPE_CONTACT)	

    address = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    picture = models.ImageField(
        upload_to='contacts/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(selft):
        return selft.name