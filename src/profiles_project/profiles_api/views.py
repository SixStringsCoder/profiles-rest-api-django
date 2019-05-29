from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


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
