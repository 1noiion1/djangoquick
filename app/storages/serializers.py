from rest_framework import serializers
from .models import Storage


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = '__all__'
        read_only_fields = ('created_at')


    def validate_inn(self, value):
        if hasattr(value, 'storage'):
            raise serializers.ValidationError('У этой компании уже есть склад')
        return value