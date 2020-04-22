from .models import InputFile
from rest_framework import serializers


class InputFileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    input_file = serializers.FileField(allow_null=True)
    input_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return InputFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.input_name = validated_data.get(
            'input_name', instance.input_name)
        instance.input_file = validated_data.get(
            'input_file', instance.input_file)
        instance.save()
        return instance


