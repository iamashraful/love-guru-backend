from rest_framework.generics import ListCreateAPIView

from api.models import Category
from api.serializers.transaction_serializers import CategorySerializer

__author__ = 'Ashraful'


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()