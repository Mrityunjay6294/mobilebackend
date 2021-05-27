from rest_framework import serializers

from Groups.models import Mygroup, MyFeeds


class MyFeedsSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFeeds
        fields = ['user_id', 'name', 'date', 'component', 'type'
                  , 'status', 'content_stripped', 'privacy',
                  'comment_count', 'favorite_count', 'group_name',
                  'group_id', 'can_delete', 'can_comment',
                  'favorited', 'can_favorite','can_edit',
                  'can_delete', 'comment_id']
