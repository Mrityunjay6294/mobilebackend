from django.contrib.sites import requests
from rest_framework import serializers
import requests

from Cources.CourseServer.CourseSererSerializer.AuthorSerializerClass import AuthorSerializerData


class CourseSerializerData(serializers.Serializer):
    """Your data serializer, define your fields here."""
    id = serializers.IntegerField()
    date = serializers.CharField()
    modified = serializers.CharField()
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    contentProtected = serializers.SerializerMethodField()
    courseServer_id = serializers.SerializerMethodField()
    AuthorData = serializers.SerializerMethodField()

    def get_AuthorData(self, obj):
        link = obj['_links']['author'][0]['href']
        response = requests.get(link)
        authdata = AuthorSerializerData(response.json())
        # l=[]
        # l.append(authdata.data)
        # print(l)
        # print(type(l))
        return authdata.data

    def get_title(self, obj):
        title = obj['title']['rendered']

        return title

    def get_content(self, obj):
        content = obj['content']['rendered']

        return content

    def get_contentProtected(self, obj):
        protected = obj['content']['protected']

        return protected

    def get_courseServer_id(self, obj):
        courseServer_id = obj['id']

        return courseServer_id
