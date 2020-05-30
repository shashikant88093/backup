from django.contrib import admin
from .models import Table

# Register your models here.
@admin.register(Table)
class BookAdmin(admin.ModelAdmin):
  list_display =['Run_ID','Date_time','Run_status','count','path','created_at']
  list_filter = ['created_at']
  search_fields = ['Run_ID']
