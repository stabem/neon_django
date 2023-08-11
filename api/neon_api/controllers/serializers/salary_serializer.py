from rest_framework import serializers
from neon_api.models import Salary


class SalarySerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(source='user.cpf', write_only=True)

    class Meta:
        model = Salary
        fields = ('id', 'date', 'amount', 'discount', 'cpf')
