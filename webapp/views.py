from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import courses
from . serializers import coursesSerializer

@api_view(['GET', 'POST'])
def courses_list(request):

    if request.method == 'GET':
        coursestemp = courses.objects.all();
        serializer = coursesSerializer(coursestemp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = coursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
