from django.contrib import admin

# Register your models here.
from .models import Post,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft','tags']
    search_fields = ['title','tags']





admin.site.register(Post,ProductAdmin)
admin.site.register(Category)