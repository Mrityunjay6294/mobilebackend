from rest_framework import serializers


from Groups.models import Mygroup


class MyGroupSerializer(serializers.Serializer):
    # specify model and fields
    # id = serializers.CharField()
    date = serializers.CharField()
    date_gmt = serializers.CharField()
    modified = serializers.CharField()
    modified_gmt = serializers.CharField()
    slug = serializers.CharField()
    status = serializers.CharField()
    groupid = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField(allow_null=True)
    content_protected = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()



    def get_groupid(self, obj):
        groupid = obj['id']

        return groupid

    def get_content(self, obj):
        content = obj['content']['rendered']

        return content

    def get_content_protected(self, obj):
        protected = obj['content']['protected']
        return str(protected)

    def get_title(self, obj):
        title = obj['title']['rendered']
        return title
