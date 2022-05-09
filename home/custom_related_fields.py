from rest_framework import serializers


class CustomRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.username} - {value.email}'