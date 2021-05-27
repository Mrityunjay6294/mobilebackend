import requests
from django.db.migrations import serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Cources.CourseServer.CourseModelSerializer.Cousre_Author_Save_Serializer import CourseSerializer
from Cources.CourseServer.CourseSererSerializer.CourseSerializerClass import CourseSerializerData

class sample(APIView):
    def post(self, request, format=None):

        saveddata = CourseSerializer(data=request.data,many=True)
        if saveddata.is_valid():
            saveddata.save()
            return Response(saveddata.data, status=status.HTTP_200_OK)
        else:
            return Response(saveddata.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response(rdata.data, status=status.HTTP_200_OK)