from django.contrib import admin
from .models import Table, Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display =['title','description','price','published']
  list_filter = ['published']
  search_fields = ['title']
admin.site.register(Table)
# admin.site.register(Book)
