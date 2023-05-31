from rest_framework import serializers
from api.models import Notes


class NoteSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(allow_null=True, required=False, max_length=200)
    body = serializers.CharField(style={
        'base_template': 'textarea.html',
    })
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Notes.objects.create(**validated_data)
    
    def update(self, validated_data, instance):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('title', instance.body)
        instance.save()
        return instance 








# class NoteSerializer(serializers.Serializer):
#     id = serializers.UUIDField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=200)
#     body = serializers.CharField(style={
#         'base_template': 'textarea.html'
#     })
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Notes.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.save()
#         return instance 