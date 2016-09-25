from django.contrib.auth.models import User, Group
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework import viewsets
from apps.subscriptions.serializers import UserSerializer, GroupSerializer

from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, \
    VerifyJSONWebToken
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer as Verifyer

from aeupdates.utils.mongo_tools import get_mongo_db


class ObtainJSONWebTokenPlainJSON(ObtainJSONWebToken):
    parser_classes = (JSONParser, )
    renderer_classes = (JSONRenderer, )


class RefreshJSONWebTokenPlainJSON(RefreshJSONWebToken):
    parser_classes = (JSONParser, )
    renderer_classes = (JSONRenderer,)


class VerifyJSONWebTokenPlainJSON(VerifyJSONWebToken):
    parser_classes = (JSONParser, )
    renderer_classes = (JSONRenderer,)


# TODO user_id should be parsable to int
def check_permissions_by_header(request, user_id=None):
    bearer = request.META['HTTP_AUTHORIZATION'].split()[-1]
    result = Verifyer().validate({'token': bearer})
    if result.get('user') and result['user'].id == int(user_id):
        return True
    return False


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    model = User

    def list(self, request):
        queryset = User.objects.all().order_by('-date_joined')
        serializer = UserSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(data=serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data['data']['attributes'])
        if settings.REGISTRATION_CLOSED:
            content = {'reason': 'Nothing to see here'}
            return Response(content, status=HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        if check_permissions_by_header(request, pk):
            queryset = User.objects.get(pk=pk)
            serializer = UserSerializer(queryset, many=False,
                                    context={'request': request})
            return Response(serializer.data)


class AeupdatesViewSet(viewsets.ModelViewSet):
    def list(self, request):
        if request.user.is_authenticated():
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True,
                                    context={'request': request})
            return Response(data=serializer.data)
        else:
            return "None"


class SubscribeToNewsBeta(viewsets.ViewSet):
    def create(self, request):
        try:
            db = get_mongo_db()
            result = db.all_emails.insert_one({'email': request.data['email']})
            return Response({'data': 'Thank you!'})
        except Exception as e:
            content = {'reason': 'Nothing to see here'}
            return Response(content, status=HTTP_403_FORBIDDEN)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
