from rest_framework import serializers
from userapp.models import User, UserProfile, Hobby


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)

        return user_list

    class Meta:
        model = Hobby
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_list = serializers.SerializerMethodField()
    
    def get_article_list(self, obj):
        article_list = []
        for article in obj.article_set.all():
            article_list.append(article.title)
        return article_list

    class Meta:
        model = User
        fields = ["username", "password", "realname", "email", "birthday", "age", "userprofile", "article_list"]
        extra_kwargs = {"password":{"write_only": True}}
