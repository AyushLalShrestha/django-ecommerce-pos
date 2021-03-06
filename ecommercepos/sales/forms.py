from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_id",
            "product_name",
            "price",
            "company_name",
            "description",
            "product_img"
        ]

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name', )

    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user




