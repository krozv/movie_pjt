from rest_framework import serializers
from .models import Review, Comment
from accounts.models import UserModel

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            fields = '__all__'
            model = UserModel
    user = UserSerializer(read_only=True) # fk 있을 경우, 이렇게 사용

    # manytomanyfield 작성하는 법 1
    # class UserLikeSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         fields = '__all__'
    #         model = UserModel
    # like_users = UserLikeSerializer(read_only=True, many=True)
    
    # manytomanyfield 작성하는 법 2
    like_users = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    
    class Meta:
        fields = '__all__'
        model = Review
