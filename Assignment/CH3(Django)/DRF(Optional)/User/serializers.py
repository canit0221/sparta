from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email", "profile_img", "bio"]
        extra_kwargs = {
            "password": {
                "write_only": True
            },  # password는 write_only로 설정 (출력 시 숨김)
        }

    def create(self, validated_data):
        # 사용자 생성 시 비밀번호를 해싱해 저장하도록 오버라이드
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  # 내부적으로 해싱
        user.save()
        return user

    def update(self, instance, validated_data):
        # 사용자 정보 수정 시 비밀번호가 포함되면 해싱 후 저장하도록 처리
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password", None)
        return data
