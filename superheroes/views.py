from superheroes.models import Heroe, Publisher
from superheroes.serializers import HeroeSerializer, PublisherSerializer
from rest_framework import generics


class HeroeList(generics.ListCreateAPIView):
    queryset = Heroe.objects.all()
    serializer_class = HeroeSerializer


class HeroeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heroe.objects.all()
    serializer_class = HeroeSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heroe.objects.all()
    serializer_class = PublisherSerializer
