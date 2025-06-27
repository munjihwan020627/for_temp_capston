### 기초 PIP 다운로드 내용
```
1.   pip install pillow
2.   pip install django
```

### 초기 실행 시 해야할 내용

```
1.   python manage.py makemigrations
2.   python manage.py migrate
3.   python manage.py runserver
```


# 미구현 내용
- common에서 가입된 회원을 channel별로 구분하여 개인별 냉장고 미 구현 (곧 구현 예정)
- find_object에서 객체 탐지 (초기 구현과 달리 GPT Vision API 구현예정)
- WMS에서 유통기한 구현
- 다른 app 생성 후 냉장고 내 물체를 통한 요리음식 추천
- 다른 app 생성 후 크롤링을 통한 쇼핑몰 연결
  
