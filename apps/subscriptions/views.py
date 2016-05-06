from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from apps.subscriptions.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    model = User

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all().order_by('-date_joined')
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
