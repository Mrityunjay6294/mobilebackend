from rest_framework import serializers

from Groups.models import Mygroup


class MyGroupSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mygroup
        fields = ['date', 'date_gmt', 'modified', 'modified_gmt', 'slug', 'status', 'groupid', 'content', 'content_protected', 'title']