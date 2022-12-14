from django import forms
from .models import WarrantyRegistration
from products.models import Product, Category


class WarrantyRegistrationForm(forms.ModelForm):

    class Meta:
        model = WarrantyRegistration
        fields = ("full_name", "email", "country", "postcode",
                  "city", "street_address1", "street_address2",
                  "products", "quantity")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cat = Category.objects.get(name='devices')
        self.fields['products'].queryset = Product.objects.filter(category=cat)
