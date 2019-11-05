# Photerest

## 사용 방법
### python 설치, 가상환경 생성 및 활성화
$ python -m venv myvenv
$ source myvenv/Scripts/activate (윈도우)
$ source myvenv/bin/activate (맥)

### 서비스에 필요한 패키지 설치
$ pip install -r requirements.txt

### git bash에서
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver