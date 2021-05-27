import json

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Groups.Serializers.MyGroupSerializerClass import MyGroupSerializer
from Groups.Serializers.MygroupSavingSerializer import MyGroupSaveSerializer
from Groups.models import Mygroup


class MygroupApiClass(APIView):
    def get(self, request):
        userid = request.data.get('userid')
        token = request.data.get('token')
        response = requests.get(f'https://demo.itlf.in/wp-json/ldlms/v2/users/{userid}/groups', headers={
            'Authorization': "Bearer " + token})

        userResponce = response.json()

        groupdata = MyGroupSerializer(userResponce, many=True)

        finaldata = MyGroupSaveSerializer(data=groupdata.data, many=True)
        if finaldata.is_valid():
            finaldata.save()
            return Response(finaldata.data, status=status.HTTP_200_OK)
        else:
            return Response(finaldata.errors, status=status.HTTP_400_BAD_REQUEST)
