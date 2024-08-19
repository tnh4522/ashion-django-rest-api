from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Offer
        fields = ['id', 'address', 'size', 'type', 'price', 'sharing', 'text', 'author']


class UserSerializer(serializers.ModelSerializer):
    offers = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'offers']
