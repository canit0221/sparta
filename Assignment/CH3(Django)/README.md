<h1>CH3 (Django)</h1>
<h2>필수과제</h2>

1) User 앱  
   • CustomUser 모델이 존재하며(프로필 이미지·소개글 추가) Django의 기본 User 모델을 확장하고 있습니다.  
   • 회원가입(signup), 로그인(login), 로그아웃(logout) 기능이 views.py와 urls.py에서 확인됩니다.  
   • 사용자 프로필 페이지(profile) 구현이 존재하며, user_profile, edit_profile 등으로 정보 수정도 가능합니다.

2) Post 앱 (CRUD)  
   • Post 모델이 존재하며, 제목·내용·작성자 등을 저장합니다.  
   • 게시글 목록 보기(post_list), 상세 보기(post_detail), 작성(post_create), 수정(post_update), 삭제(post_delete) 기능이 구현되어 있습니다.

3) 기본 템플릿  
   • base.html, navbar.html, footer.html 구조가 확인됩니다.  
   • base.html에서 navbar.html을 include하여 네비게이션 바를, footer.html을 include하여 푸터를 표시하고 있습니다.

4) 데이터베이스  
   • SQLite3 사용 (settings.py와 db.sqlite3 확인).


<hr>

<h2>선택과제</h2>
아래와 같이 확인되었습니다: 

1) DRF(Django Rest Framework)로 변환  
   • User와 Post 모두를 위해 serializers.py에 Serializer 클래스들이 구현되어 있습니다. (UserSerializer, PostSerializer, CommentSerializer, LikeSerializer 등)  
   • API 뷰(views.py)에서도 Post, Comment, Like에 대해 RESTful CRUD가 가능하도록 설계되었습니다.


2) 좋아요 기능  
   • Like 모델(Post 모델과 1:N, user와 1:N)을 통해 좋아요가 구현되어 있습니다.  
   • LikeSerializer가 존재하며, PostDetailSerializer에 like_set을 직렬화해서 likes_count 수를 세도록 구현되어 있습니다.

3) 댓글 기능  
   • Comment 모델(Post와 1:N 관계) 및 CommentSerializer가 존재합니다. 
   • PostDetailSerializer에 comment_set을 직렬화해서 comments_count 수를 세도록 구현되어 있습니다.

4) 데이터베이스 (SQLite3에서 PostgreSQL or MySQL로 마이그레이션)  
   • 현재 config/settings.py 등에서 DB 설정을 보면 여전히 SQLite3가 사용되고 있음
   • MySQL이나 PostgreSQL로 변경한 흔적은 찾지 못함  

