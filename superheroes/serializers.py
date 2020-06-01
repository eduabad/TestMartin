from rest_framework import serializers

from .models import Publisher
from .models import Heroe


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'founder')


class HeroeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroe
        fields =('id', 'name', 'gender', 'real_name', 'publisher' )
