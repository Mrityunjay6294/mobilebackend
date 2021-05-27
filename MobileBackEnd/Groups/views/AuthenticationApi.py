import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthenticationClass(APIView):
    def get(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        userdata = {'username': username, 'password': password}
        response = requests.post('https://demo.itlf.in/wp-json/jwt-auth/v1/token', data=userdata)
        userResponce = response.json()
        return Response(userResponce, status=status.HTTP_200_OK)

