# Pure Django(Essential) 프로젝트

이 프로젝트는 Django 5.1.5 및 관련 라이브러리를 활용하여 가장 기본적인 웹 애플리케이션 구조를 구현한 예시 코드입니다.

## 요구 사항 (Requirements)
아래와 같은 라이브러리가 필요하며, 프로젝트 루트 디렉토리에 포함된 requirements.txt 파일을 통해 쉽게 설치할 수 있습니다:
- Django==5.1.5
- django-extensions
- django-seed
- Pillow
- Faker
- python-dateutil
- sqlparse
- typing_extensions
- asgiref
- six
- toposort

## 프로젝트 구조
- **config**: Django 설정 및 URL 라우팅을 관리하는 폴더
  - settings.py: 기본 설정, INSTALLED_APPS, DATABASE 설정 등이 포함  
  - urls.py: 전체 프로젝트 URL 경로 설정
- **User** 앱:
  - 사용자 관련 모델, 뷰, 인증 로직 등을 관리
- **Post** 앱:
  - 게시물 관련 모델, 뷰 등을 관리
- **templates** 폴더:
  - HTML 템플릿을 저장하여 Django의 템플릿 엔진과 연동
- **media** 폴더:
  - 사진, 파일 등의 업로드 미디어 파일 저장 폴더
- **db.sqlite3**: SQLite 데이터베이스 파일
- **manage.py**: Django 프로젝트를 관리하기 위한 명령행 인터페이스

## 설치 및 설정
1. (선택) 가상환경 생성 및 활성화 (권장):
   ```
   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   .\venv\Scripts\activate   # Windows
   ```
2. 프로젝트 디렉토리로 이동:
   ```
   cd Assignment/CH3(Django)/Pure_Django(Essential)
   ```
3. 필요한 패키지 설치:
   ```
   pip install -r requirements.txt
   ```

## 데이터베이스 마이그레이션
프로젝트 최초 실행 전에 아래 명령어로 마이그레이션을 적용합니다:
```
python manage.py migrate
```

## 더미 데이터 생성
django-seed를 활용해 더미 데이터를 생성할 수 있습니다. 예를 들어:
```
python manage.py seed User --number=10
python manage.py seed Post --number=10
```
(숫자는 예시이며 필요에 맞게 변경 가능)

## 서버 실행
아래 명령어를 통해 개발 서버를 실행하고, 브라우저에서 [http://127.0.0.1:8000](http://127.0.0.1:8000) 로 접속하여 동작을 확인할 수 있습니다.
```
python manage.py runserver
```

## 배포 시 고려 사항
- DEBUG 모드를 꺼야 합니다.
- SECRET_KEY를 노출하지 않도록 주의합니다.
- 실제 운영 환경에 맞추어 ALLOWED_HOSTS, 데이터베이스 설정, HTTPS 설정 등을 변경해 주어야 합니다.

이상으로 Pure Django(Essential) 프로젝트에 대한 간단한 안내를 마칩니다.