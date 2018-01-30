from rest_framework import serializers
from . models import courses

class coursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = courses
        #fields=('firstname', 'lastname')
        fields='__all__'