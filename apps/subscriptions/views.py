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

    def list(self, request):
        queryset = User.objects.all().order_by('-date_joined')
        serializer = UserSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(data=serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data['data']['attributes'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AeupdatesViewSet(viewsets.ModelViewSet):
    def list(self, request):
        if request.user.is_authenticated():
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True,
                                    context={'request': request})
            return Response(data=serializer.data)
        else:
            return "None"


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
