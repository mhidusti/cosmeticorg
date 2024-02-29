from django.db import models
from accounts.models import CustomeUser
from product.models import Products


class OrderBy(models.Model):
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    zarinpal_authority = models.CharField(max_length=200, blank=True)
    zarinpal_refid = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)
    is_paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'Order : {self.id}'
    
    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())
    
    def __iter__(self):
        for item in self.items.all():
            yield item

class OrderItem(models.Model):
    order = models.ForeignKey(OrderBy, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'product item {self.id} for Order {self.order.id}'
