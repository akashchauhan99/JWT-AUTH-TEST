from django.http.response import Http404
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from ..models import Language, Paradigm, Programmer

# for language view
class LanguageView(APIView):
    # we need to put permission_classes in every view for permission 
    # but if we provide it in settings it'll work for entire project
    # so you can add it as REST_FRAMEWORK in settings
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  
    def get(self, request):
        language = Language.objects.all()
        serializer = LanguageSerializer(language, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LanguageDetailView(APIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        print(language)
        serializers = LanguageSerializer(language)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        language = self.get_object(pk)
        print(language)
        serializers = LanguageSerializer(language, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        language = self.get_object(pk)
        print(language)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# for paradigm view
class ParadigmView(APIView):
    def get(self, request):
        language = Paradigm.objects.all()
        serializer = ParadigmSerializer(language, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ParadigmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParadigmDetailView(APIView):
    def get_object(self, pk):
        try:
            return Paradigm.objects.get(pk=pk)
        except Paradigm.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        paradigm = self.get_object(pk)
        print(paradigm)
        serializers = ParadigmSerializer(paradigm)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        paradigm = self.get_object(pk)
        print(paradigm)
        serializers = ParadigmSerializer(paradigm, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        paradigm = self.get_object(pk)
        print(paradigm)
        paradigm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# for programmer view
class ProgrammerView(APIView):
    def get(self, request):
        language = Programmer.objects.all()
        serializer = ProgrammerSerializer(language, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProgrammerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgrammerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Programmer.objects.get(pk=pk)
        except Programmer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        programmer = self.get_object(pk)
        print(programmer)
        serializers = ProgrammerSerializer(programmer)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        programmer = self.get_object(pk)
        print(programmer)
        serializers = ProgrammerSerializer(programmer, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        programmer = self.get_object(pk)
        print(programmer)
        programmer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)