from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, name=None):
        name = name.lower()
        if name.endswith('/'):
            name = name[:-1]
        try:
            queryset = Product.objects.get(name=name)
        except Product.DoesNotExist:
            return Response("Not Exist",
                            status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(queryset, many=False,
                       context={'request': request})
        return Response(serializer.data)

