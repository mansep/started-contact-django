from django import forms

class ContactForm(forms.Form):

    id_document = forms.CharField(max_length=50) #Chile RUT/RUN, Perú RUC/DNI, España, Argentina DNI, México RFC/CURP https://es.wikipedia.org/wiki/Documento_de_identidad
    name = forms.CharField(max_length=60, required=True)
    type = forms.CharField(max_length=1, required=True)	

    address = forms.CharField(max_length=200, required=False)
    state = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=20, required=False)
    fax = forms.CharField(max_length=20, required=False)
    mobile = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=254, required=False)
    website = forms.URLField(max_length=200, required=False)

    picture = forms.ImageField(required=False)