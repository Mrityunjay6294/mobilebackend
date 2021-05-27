from rest_framework import serializers

from Groups.models import Mygroup


class MyFeedSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    date = serializers.CharField(max_length=50)
    component = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=500)
    status = serializers.CharField(max_length=500)
    content_stripped = serializers.CharField(max_length=1000)
    privacy = serializers.CharField(max_length=10)

    comment_count = serializers.CharField(max_length=10)
    favorite_count = serializers.CharField(max_length=50)

    group_name = serializers.SerializerMethodField()
    group_id = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    can_comment = serializers.SerializerMethodField()
    favorited = serializers.SerializerMethodField()
    can_favorite = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    comment_id = serializers.SerializerMethodField()

    def get_group_name(self, obj):
        group_name = obj['activity_data']['group_name']

        return group_name

    def get_group_id(self, obj):
        group_id = obj['activity_data']['group_id']

        return group_id

    def get_can_delete(self, obj):
        can_delete = obj['can_delete']

        return str(can_delete)

    def get_can_comment(self, obj):
        can_comment = obj['can_comment']

        return str(can_comment)

    def get_favorited(self, obj):
        favorited = obj['favorited']
        return str(favorited)

    def get_can_favorite(self, obj):
        can_favorite = obj['can_favorite']
        return str(can_favorite)

    def get_can_edit(self, obj):
        can_edit = obj['can_edit']
        return str(can_edit)

    def get_can_delete(self, obj):
        can_delete = obj['can_delete']
        return str(can_delete)

    def get_comment_id(self, obj):
        comment_id = obj['id']

        return str(comment_id)
