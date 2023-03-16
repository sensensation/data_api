from rest_framework import serializers


class PingPongSerializer(serializers.Serializer):
    ping = serializers.CharField(
        allow_blank=True,
        default="ping",
        max_length=20,
        help_text="please input 'ping'"
    )