import json

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_json_api.renderers import JSONRenderer

from apps.products.models import Product
from apps.news.models import News
from apps.products.serializers import ProductSerializer


# TODO: Response from server now is pure JSON, not DRF web page with data :(
# TODO: ATTENTION THIS IS SUPER BAD HACK!

class SortedRelationsRenderer(JSONRenderer):
    """
    Custom JSONRenderer class, used to sort relationships by custom field.
    Can't being achieved in other way, because DjangoJSONAPI library sorts results
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        obj = super(SortedRelationsRenderer, self).render(data, accepted_media_type, renderer_context)
        obj = json.loads(obj.decode('utf-8'))
        obj['data']['relationships']['news']['data'] = sorted(obj['data']['relationships']['news']['data'],
                                                              key=lambda el: News.objects.get(id=el['id']).version, reverse=True)
        obj = json.dumps(
            obj, cls=self.encoder_class, ensure_ascii=self.ensure_ascii,
        )
        obj = obj.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        return bytes(obj.encode('utf-8'))


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

