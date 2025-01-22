from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

CustomUser = get_user_model()


class UserCreateView(APIView):
    """
    UserCreateView 클래스는 사용자의 회원가입을 처리하는 APIView입니다.
    메서드:
        post(self, request):
            회원가입 요청을 처리합니다.
            유효한 데이터가 제공되면 사용자를 생성하고 201 상태 코드를 반환합니다.
            유효하지 않은 데이터가 제공되면 400 상태 코드를 반환합니다.
    """

    def post(self, request):  # 회원가입
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # 비밀번호 해싱 포함
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    """
    UserDetailView 클래스는 사용자 프로필 조회, 수정, 삭제 기능을 제공합니다.
    메서드:
        - get(self, request, pk): 주어진 pk에 해당하는 사용자의 프로필을 조회합니다.(프로필 조회)
        - patch(self, request, pk): 주어진 pk에 해당하는 사용자의 정보를 수정합니다.(회원정보 수정)
        - delete(self, request, pk): 주어진 pk에 해당하는 사용자를 삭제합니다.(회원탈퇴)
    """

    def get(self, request, pk):  # 프로필 조회
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):  # 회원정보 수정
        user = get_object_or_404(CustomUser, pk=pk)
        if request.user == user:  # 본인인증
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  # 비밀번호 해싱 포함
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
        )  # 권한 없음

    def delete(self, request, pk):  # 회원탈퇴
        user = get_object_or_404(CustomUser, pk=pk)
        if request.user == user:  # 본인인증
            user.delete()  # 사용자 삭제
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
        )  # 권한 없음


class LogoutView(APIView):  # 로그아웃
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # request.data에서 refresh token을 가져온다고 가정
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # blacklist에 등록

            return Response(
                {"detail": "로그아웃 되었습니다."}, status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"detail": "토큰이 유효하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
