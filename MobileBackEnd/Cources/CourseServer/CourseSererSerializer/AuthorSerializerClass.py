from rest_framework import serializers


class AuthorSerializerData(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    slug = serializers.CharField()
    url = serializers.SerializerMethodField()
    AuthorServer_id = serializers.SerializerMethodField()


    def get_url(self, obj):
        link = obj['avatar_urls']['96']

        return link

    def get_AuthorServer_id(self, obj):
        AuthorServer_id = obj['id']

        return AuthorServer_id