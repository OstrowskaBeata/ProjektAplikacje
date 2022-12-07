from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Zlecenia, Kierowca, Ciezarowka, LADUNEK, MARKA
from .serializers import KierowcaSerializer, ZleceniaSerializer, CiezarowkaSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


@api_view(['GET'])
def kierowca_list(request):
    if request.method == 'GET':
        kierowca = Kierowca.objects.all()
        serializer = KierowcaSerializer(kierowca, many=True)
        return Response(serializer.data)
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

@api_view(['GET'])
def kierowca_detail(request, pk):
    try:
        kierowca = Kierowca.objects.get(pk=pk)
    except Kierowca.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        kierowca = Kierowca.objects.get(pk=pk)
        serializer = KierowcaSerializer(kierowca)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def kierowca_update_delete(request, pk):
    try:
        kierowca = Kierowca.objects.get(pk=pk)
    except Kierowca.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = KierowcaSerializer(kierowca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kierowca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def kierowca_imie(request,imie):
    if request.method == 'GET':
        kierowca = Kierowca.objects.filter(imie=imie)
        serializer = KierowcaSerializer(kierowca, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def kierowca_add(request):
    if request.method == 'POST':
        serializer = KierowcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ciezarowki_list(request):
    if request.method == 'GET':
        ciezarowki = Ciezarowka.objects.all()
        serializer = CiezarowkaSerializer(ciezarowki, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ciezarowki_detail(request, pk):
    try:
        ciezarowki = Ciezarowka.objects.get(pk=pk)
    except Ciezarowka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ciezarowki = Ciezarowka.objects.get(pk=pk)
        serializer = CiezarowkaSerializer(ciezarowki)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def ciezarowki_update_delete(request, pk):
    try:
        ciezarowki = Ciezarowka.objects.get(pk=pk)
    except Ciezarowka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CiezarowkaSerializer(ciezarowki, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ciezarowki.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def ciezarowki_add(request):
    if request.method == 'POST':
        serializer = CiezarowkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def zlecenia_list(request):
    if request.method == 'GET':
        zlecenia = Zlecenia.objects.all()
        serializer = ZleceniaSerializer(zlecenia, many=True)
        return Response(serializer.data)
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

@api_view(['GET'])
def zlecenia_detail(request, pk):
    try:
        zlecenia = Zlecenia.objects.get(pk=pk)
    except Zlecenia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zlecenia = Zlecenia.objects.get(pk=pk)
        serializer = ZleceniaSerializer(zlecenia)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def zlecenia_update_delete(request, pk):
    try:
        zlecenia = Zlecenia.objects.get(pk=pk)
    except Zlecenia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ZleceniaSerializer(zlecenia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        zlecenia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST'])
def zlecenia_add(request):
    if request.method == 'POST':
        serializer = ZleceniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)