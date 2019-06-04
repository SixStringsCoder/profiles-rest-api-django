from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions



class HelloAPIView(APIView):
    """ Test API View """

    # the serializer used to describe the data with this API view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """

        an_apiview = [
            'Uses HTTP methods as function (get, pst, patch, put, delete',
            'Similar to a traditional Django view',
            'Give you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview })

    # the logic that gets called when an HTTP POST request is made to the APIView
    def post(self, request):
        """ Create a hello message with our name. """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f"Hello, {name}."
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object """

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request only updates the fields provided in the request """

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object """

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """

    # the serializer used to describe the data with this API view
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return HelloAPIView Msg """

        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code"
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new hello message """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f"Hello {name} using the viewset"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting an object by its id """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handles updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles updating part of an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Deletes an object """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading an updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """ Checks email and password and return an auth token """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToekn apiview to validate and create a token"""

        return ObtainAuthToken().post(request)
