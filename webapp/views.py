from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import courses
from . serializers import coursesSerializer

class coursesList(APIView):

    def get(self, request):
        coursestemp = courses.objects.all();
        serializer = coursesSerializer(coursestemp, many=True)
        return Response(serializer.data)

    def post(self):
        pass


