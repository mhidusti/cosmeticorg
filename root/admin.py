from django.contrib import admin
from .models import *


class AdminServices(admin.ModelAdmin):

    list_display = ['title', 'content', 'status']
    list_filter = ['status']
    search_fields = ['title']

admin.site.register(ContactUs)
admin.site.register(Comment)
admin.site.register(Social)
admin.site.register(Gallery)
admin.site.register(Product_Feature)
admin.site.register(Pack_Products)
admin.site.register(Special_Products)
