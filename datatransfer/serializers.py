from rest_framework import serializers
from datatransfer.models import CsvFile, Purchase


class PingPongSerializer(serializers.Serializer):
    ping = serializers.CharField(
        allow_blank=True,
        default="ping",
        max_length=20,
        help_text="please input 'ping'"
    )


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = "__all__"


class CsvFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CsvFile
        fields = "__all__"
