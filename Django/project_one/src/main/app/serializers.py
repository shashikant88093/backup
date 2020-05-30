from rest_framework import serializers
from .models import Book,Table


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['id','title','description','price','published','cover','is_published']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields=['Run_ID','Run_status','count','path','Date_time']