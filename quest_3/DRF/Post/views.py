from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PostListAPIView(APIView):
    def get(self, request):  # get요청시 게시글 목록조회
        posts = Post.objects.all()  # 모든 Post 객체를 가져온다.
        serializer = PostSerializer(
            posts, many=True
        )  # PostSerializer를 사용하여 직렬화한다. many=True는 여러 객체를 직렬화할 때 사용한다.
        return Response(serializer.data)  # 직렬화된 데이터를 반환한다.

    def post(self, request):  # post요청시 새로운 게시글 생성
        serializer = PostSerializer(
            data=request.data
        )  # 직렬화할 데이터를 PostSerializer에 넣는다.
        if serializer.is_valid(raise_exception=True):  # 데이터가 유효한지 확인한다.
            serializer.save()  # 데이터 저장
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # 저장된 데이터를 반환한다.


class PostDetailAPIView(APIView):
    def get_object(
        self, pk
    ):  # pk에 해당하는 Post 객체가 없을 경우 404에러를 반환하는 함수
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):  # get요청시 특정 게시글 상세조회
        post = self.get_object(pk=pk)  # pk에 해당하는 Post 객체를 가져온다.
        serializer = PostSerializer(post)  # PostSerializer를 사용하여 직렬화한다.
        return Response(serializer.data)  # 직렬화된 데이터를 반환한다.

    def put(self, request, pk):  # put요청시 특정 게시글 수정
        post = self.get_object(pk=pk)  # pk에 해당하는 Post 객체를 가져온다.
        serializer = PostSerializer(
            post, data=request.data, partial=True
        )  # PostSerializer를 사용하여 직렬화한다,
        # data에 수정할 데이터를 넣는다.(instance와 같은 역할),
        # partial=True로 설정하면 일부 필드만 수정할 수 있다.
        if serializer.is_valid(raise_exception=True):  # 데이터가 유효한지 확인한다.
            serializer.save()  # 데이터 저장
            return Response(serializer.data)  # 저장된 데이터를 반환한다.

    def delete(self, request, pk):  # delete요청시 특정 게시글 삭제
        post = self.get_object(pk=pk)  # pk에 해당하는 Post 객체를 가져온다.
        post.delete()  # Post 객체 삭제
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )  # 삭제 성공시 204 No Content 반환
