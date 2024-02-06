from django.contrib import admin
from .models import ContactUsForm, OrderForm, CommentForm, Social, Gallery, Pack_Products, Special_Products, Products,Best_Products,  Product_Feature, Category 


class AdminServices(admin.ModelAdmin):

    list_display = ['title', 'content', 'status']
    list_filter = ['status']
    search_fields = ['title']

admin.site.register(ContactUsForm)
admin.site.register(OrderForm)
admin.site.register(CommentForm)
admin.site.register(Social)
admin.site.register(Gallery)
admin.site.register(Pack_Products)
admin.site.register(Special_Products)
admin.site.register(Best_Products)
admin.site.register(Products)
admin.site.register(Product_Feature)
admin.site.register(Category)