from rest_framework import serializers

from models import Subscription


class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("id",)
