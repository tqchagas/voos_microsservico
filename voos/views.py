from voos.models import Aeroporto, Voo
from voos.serializers import AeroportoSerializer, VooSerializer
from rest_framework import generics


class AeroportoView(generics.ListCreateAPIView):
    queryset = Aeroporto.objects.all()
    serializer_class = AeroportoSerializer


class VooCriarListar(generics.ListCreateAPIView):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer


class VooDetalheApagar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer
