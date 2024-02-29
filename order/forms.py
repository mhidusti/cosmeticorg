from django import forms
from .models import OrderBy, OrderItem

class OrderByFrom(forms.ModelForm):

    class Meta:
        model = OrderBy
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']