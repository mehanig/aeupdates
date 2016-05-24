from rest_framework import viewsets
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, pk=None):
        if pk.endswith('/'):
            pk = pk[:-1]
        queryset = Product.objects.get(url__endswith=pk)
        serializer = ProductSerializer(queryset, many=False,
                       context={'request': request})
        return Response(serializer.data)
