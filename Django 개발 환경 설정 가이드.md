# Django 개발 환경 설정 가이드

1. **가상환경 생성 / 실행**
   - 생성
   
   ```bash
   python -m venv [가상환경 이름]
   ```
   
   - 실행
   
   ```bash
   source [가상환경 이름]/Scripts/activate
   ```
   
   - 가상환경 끄기
   
   ```bash
   deactivate
   ```
2.  **Django LTS 버전 설치 (가상환경 위에서)**
   
   ```bash
   pip install django==3.2.13
   ```



3.  **Django 프로젝트 생성**
   
   ```bash
   django-admin startproject [프로젝트이름] .
   ```

4.  **Django 실행**
   
   ```bash
   python manage.py runserver
   ```
   
   -> 주소창에 localhost:8000 하면 성공





> 그외 것들... + 모든 명령은 bash에서...

- 가상환경 삭제 
  
  - rm -r [가상환경 이름]

- /: root

- ~: home

       








