from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import Post, Comment, Like
from .serializers import (
    PostSerializer,
    PostDetailSerializer,
    CommentSerializer,
    LikeSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required


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
        serializer = PostDetailSerializer(
            post
        )  # PostDetailSerializer를 사용하여 직렬화한다.
        return Response(serializer.data)  # 직렬화된 데이터를 반환한다.

    def put(self, request, pk):  # put요청시 특정 게시글 수정
        post = self.get_object(pk=pk)  # pk에 해당하는 Post 객체를 가져온다.
        serializer = PostDetailSerializer(
            post, data=request.data, partial=True
        )  # PostDetailSerializer를 사용하여 직렬화한다,
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


class CommentListAPIView(APIView):
    """
    CommentListAPIView는 특정 게시글의 댓글 목록을 반환하고 댓글을 생성하는 API 뷰입니다.
    메서드:
        get(self, request, pk):
            주어진 pk에 해당하는 게시글의 댓글 목록을 반환합니다.
            Args:
                pk (int): 게시글의 기본 키
            Returns:
                Response: 직렬화된 댓글 데이터를 포함한 응답
        post(self, request, pk):
            주어진 pk에 해당하는 게시글에 댓글을 생성합니다.
            Args:
                pk (int): 게시글의 기본 키
            Returns:
                Response: 직렬화된 댓글 데이터를 포함한 응답
    """

    def get(self, request, post_pk):  # 게시글의 댓글 목록을 반환하는 함수
        post = get_object_or_404(Post, pk=post_pk)  # pk에 해당하는 게시글을 가져옴
        comments = post.comment_set.all()  # 게시글에 해당하는 모든 댓글을 가져옴
        serializer = CommentSerializer(
            comments, many=True
        )  # 댓글을 직렬화, many=True는 여러 개의 데이터를 직렬화할 때 사용
        return Response(serializer.data)  # 직렬화한 데이터를 반환

    def post(self, request, post_pk):  # 게시글에 댓글을 생성하는 함수
        post = get_object_or_404(Post, pk=post_pk)  # pk에 해당하는 게시글을 가져옴
        serializer = CommentSerializer(data=request.data)  # 직렬화할 데이터를 받아옴
        if serializer.is_valid(
            raise_exception=True
        ):  # 데이터가 유효한지 확인, 유효하지 않으면 오류 발생 (400 Bad Request)
            serializer.save(
                post=post
            )  # 데이터 저장, post는 댓글이 달릴 게시글 (post 필드에 post를 넣어줌)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # 직렬화한 데이터를 반환, status=201은 생성됨을 의미


class CommentDetailAPIView(APIView):
    def get_object(self, comment_pk):  # pk에 해당하는 댓글을 가져오는 함수
        return get_object_or_404(Comment, pk=comment_pk)

    def delete(self, request, comment_pk):  # 댓글을 삭제하는 함수
        comment = self.get_object(pk=comment_pk)  # pk에 해당하는 댓글을 가져옴
        comment.delete()  # 댓글 삭제
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )  # status=204는 성공했지만 반환할 데이터가 없음을 의미

    def put(self, request, comment_pk):  # 댓글을 수정하는 함수
        comment = self.get_object(pk=comment_pk)  # pk에 해당하는 댓글을 가져옴
        serializer = CommentSerializer(
            comment, data=request.data
        )  # 직렬화할 데이터를 받아옴, comment는 수정할 댓글 (instance와 같은 역할)
        if serializer.is_valid(
            raise_exception=True
        ):  # 데이터가 유효한지 확인, 유효하지 않으면 오류 발생 (400 Bad Request)
            serializer.save()  # 데이터 저장
            return Response(serializer.data)  # 직렬화한 데이터를 반환
