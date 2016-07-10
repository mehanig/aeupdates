from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
from rest_framework.renderers import JSONRenderer
from rest_framework_json_api.renderers import JSONRenderer

from apps.products.models import Product
from apps.news.models import News
from apps.products.serializers import ProductSerializer


class SortedRelationsRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = data
        obj = super(SortedRelationsRenderer, self).render(data, accepted_media_type, renderer_context)
        return obj


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (SortedRelationsRenderer,)

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

