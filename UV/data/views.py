from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from .models import UV
from .serializer import UVSerializer


class UVListCreateAPIView(generics.ListCreateAPIView):
    queryset = UV.objects.all()
    serializer_class = UVSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get(self, request, *args, **kwargs):
        instance = self.queryset.latest('created_at')
        if instance is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

