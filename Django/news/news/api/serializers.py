from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        # user: UserCreateSerializers(read_only=True)
        model = Table
        fields = (
            'Run_ID',
            'Date_time',
            'Run_status',
            'count',
            'path',
            'created_at'
        )