from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Wallet
from api.serializers.transaction_serializers import WalletSerializer

__author__ = 'Ashraful'


class WalletListView(ListCreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = WalletSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            raise Http404
