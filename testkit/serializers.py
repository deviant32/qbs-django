from rest_framework import serializers
from .models import TestKit


class TestKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestKit
        fields = '__all__'
