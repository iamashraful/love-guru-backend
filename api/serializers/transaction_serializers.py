from rest_framework.serializers import ModelSerializer

from api.models import Category, Wallet, Transaction

__author__ = 'Ashraful'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'created_at', 'updated_at')


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('pk', 'name', 'balance', 'initial_balance', 'is_active', 'created_at', 'updated_at')


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('pk', 'name', 'category', 'wallet', 'transaction_time', 'amount', 'created_at', 'updated_at')
