from rest_framework import serializers
from base.models import Item
from machine_learning.models import CustomerChurn

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CustomerChurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerChurn
        fields = '__all__'