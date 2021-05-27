from rest_framework import serializers

from Cources.models import Cources, Author


class AuthorSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Author
        fields = ['name', 'description', 'url','AuthorServer_id']


class CourseSerializer(serializers.ModelSerializer):
    AuthorData = AuthorSerializer()

    class Meta:
        model = Cources
        fields = ['date', 'courseServer_id',  'modified', 'content', 'contentProtected','AuthorData']
