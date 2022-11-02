from rest_framework import serializers

from .models import Perk, Experience

from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "name",
            "details",
            "explanation", 
        )
        

class ExperienceSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Experience
        exclude = (
            "perks",
            "created_at",
            "updated_at",
            "host",
            "city",
            "address",
            "description",
        )

class ExperienceDetailSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(many=True, read_only=True)

    is_host = serializers.SerializerMethodField()

    def get_is_host(self, experience):
        request = self.context['request']
        return experience.host == request.user


    class Meta:
        model = Experience
        exclude = (
            "created_at",
            "updated_at",
        )