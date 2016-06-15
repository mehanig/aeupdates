from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):

    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request):
        if request.user.is_authenticated():
            queryset = News.objects.all()
            serializer = NewsSerializer(queryset, many=True,
                                    context={'request': request})
            return Response(data=serializer.data)
        else:
            return "None"