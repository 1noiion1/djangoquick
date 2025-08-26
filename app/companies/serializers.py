from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')


    def validate_inn(self, value):
        if not value.isdigit() or len(value) not in [10, 12]:
            raise serializers.ValidationError('ИНН должен состоять из 10 или 12 цифр')
        return value