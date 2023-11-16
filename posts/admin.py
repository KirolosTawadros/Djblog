from django.contrib import admin

# Register your models here.
from .models import Post,Category,Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft','tags','id']
    search_fields = ['title','tags']





admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)