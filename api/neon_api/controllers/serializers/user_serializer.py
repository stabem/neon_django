from rest_framework import serializers
from neon_api.domain.user import User


class UserSerializer(serializers.Serializer):
    cpf = serializers.CharField(max_length=11)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        return instance
