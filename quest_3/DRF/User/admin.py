from django.contrib import admin  # Django의 admin 모듈을 가져옵니다.
from django.contrib.auth.admin import (
    UserAdmin,
)  # 사용자 관리에 필요한 UserAdmin 클래스를 가져옵니다.
from .models import CustomUser  # CustomUser 모델을 가져옵니다.

# CustomUser 모델을 admin에 등록합니다.
admin.site.register(
    CustomUser, UserAdmin
)  # CustomUser를 UserAdmin을 사용하여 admin에 등록합니다.
