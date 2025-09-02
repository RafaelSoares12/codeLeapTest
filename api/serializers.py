from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "username", "created_datetime", "title", "content"]
        read_only_fields = ["id","created_datetime"]

    def update(self, instance, validated_data):
        forbidden = set(validated_data.keys()) - {"title","content"}
        if forbidden:
            raise serializers.ValidationError({"detail":"only title and content can be updated"})
        return super().update(instance, validated_data)
