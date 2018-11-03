from rest_framework import serializers
from voos.models import Aeroporto, Voo


class AeroportoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Aeroporto


class VooSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Voo
