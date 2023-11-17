from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Post,Category,Comment

class ProductAdmin(SummernoteModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft','tags','id']
    search_fields = ['title','tags']
    summernote_fields = ('content',)





admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)