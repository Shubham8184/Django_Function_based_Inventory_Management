from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display=['id','date','provider','productname','price','qty','amount','stock']

admin.site.register(Product,ProductAdmin)
