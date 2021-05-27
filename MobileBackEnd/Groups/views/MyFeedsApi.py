import json

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Groups.Serializers.MyFeedSerializerClass import MyFeedSerializer
from Groups.Serializers.MyFeedsSavingSerializers import MyFeedsSaveSerializer


class MyFeedsApiClass(APIView):
    def get(self, request):

        token = request.data.get('token')
        response = requests.get('https://demo.itlf.in/wp-json/buddyboss/v1/activity', headers={
            'Authorization': "Bearer " + token})

        userResponce = response.json()

        groupdata = MyFeedSerializer(userResponce, many=True)

        finaldata = MyFeedsSaveSerializer(data=groupdata.data, many=True)
        if finaldata.is_valid():
            finaldata.save()
            return Response(finaldata.data, status=status.HTTP_200_OK)
        else:
            return Response(finaldata.errors, status=status.HTTP_400_BAD_REQUEST)
