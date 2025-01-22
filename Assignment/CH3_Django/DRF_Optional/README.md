# DRF(Optional) 프로젝트

이 프로젝트는 Django 5.1.5와 Django REST Framework를 활용하여 구현한 예시 코드입니다.

## 요구 사항 (Requirements)
아래와 같은 라이브러리가 필요하며, 프로젝트 루트 디렉토리에 포함된 requirements.txt 파일에 명시되어 있습니다:
- Django==5.1.5
- djangorestframework
- django-extensions
- django-seed
- rest_framework_simplejwt (JWT 인증에 사용)
- pillow
- Faker
- python-dateutil
- sqlparse
- typing_extensions

## 설치 방법
1. (선택) 가상환경 생성 및 활성화 (권장):
   ```
   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   .\venv\Scripts\activate   # Windows
   ```
2. 프로젝트 디렉토리로 이동:
   ```
   cd Assignment/CH3(Django)/DRF(Optional)
   ```
3. 필요한 패키지 설치:
   ```
   pip install -r requirements.txt
   ```

## 프로젝트 구조
- **config**: Django 설정 및 URL 라우팅을 관리하는 폴더
  - settings.py: 기본 설정, INSTALLED_APPS, DATABASE 설정 등이 포함됨
  - urls.py: 전체 프로젝트 URL 경로 설정
- **User** 앱:
  - CustomUser 모델을 정의 (AUTH_USER_MODEL로 사용)
  - 사용자 관련 인증, 직렬화(serializers.py), 뷰(views.py) 등 포함
- **Post** 앱:
  - 게시물 관련 모델, 직렬화(serializers.py), 뷰(views.py) 등 포함
- **manage.py**: Django 프로젝트를 관리하기 위한 명령행 인터페이스

## 실행 방법
1. 프로젝트 루트 디렉토리(여기서 manage.py가 있는 위치)에서 서버 실행:
   ```
   python manage.py runserver
   ```
2. 웹 브라우저에서 http://127.0.0.1:8000 으로 접속하여 동작을 확인

## 주요 설정
- `INSTALLED_APPS`에 Django REST Framework, django_seed, rest_framework_simplejwt.token_blacklist 등이 등록되어 있습니다.
- SQLite3를 기본 데이터베이스로 사용합니다.
- `REST_FRAMEWORK` 설정에서 JWT 인증을 기본으로 사용하며, 권한 정책으로 `IsAuthenticated`가 적용되어 있습니다.
- SECRET_KEY와 DEBUG 값은 교육 목적으로 설정되어 있으며, 실제 배포 시 보안을 위해 별도의 환경 변수 등을 사용하는 것이 좋습니다.

## JWT 인증
- Simple JWT를 이용하여 JWT 생성 및 검증을 진행합니다.
- 로그인/회원가입 로직에 따라 토큰 발급 후, API 요청 시 Authorization 헤더에 `Bearer <token>` 형태로 전송합니다.

## 마이그레이션 & 더미 데이터
- 마이그레이션:
  ```
  python manage.py migrate
  ```
- 더미 데이터 생성(django-seed 사용 시):
  ```
  python manage.py seed User --number=10
  python manage.py seed Post --number=10
  ```
  (해당 숫자는 예시이며, models.py나 각 시드 설정에 맞게 조정 가능)

## 추가 사항
- REST API 엔드포인트에 대한 구체적인 내용은 User/urls.py, Post/urls.py 등을 참고하세요.
- DRF(Optional) 프로젝트는 Django + DRF 학습 및 실습용 예시이며, 실제 환경에 배포할 때는 반드시 디버그 모드를 끄고 배포 환경에 맞도록 설정을 변경해야 합니다.

