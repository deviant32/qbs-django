from rest_framework import serializers
from rest_auth.models import TokenModel
from .models import User
from testkit.models import TestKit
from testkit.serializers import TestKitSerializer


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenModel
        fields = "__all__"


class UserDetailsSerializer(serializers.ModelSerializer):
    testkits = serializers.PrimaryKeyRelatedField(
        queryset=TestKit.objects.all(), many=True)

    class Meta:
        model = User
        exclude = ("password",)
