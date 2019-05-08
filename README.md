# README

## 프로젝트 설명
본 프로젝트는 REST API의 예시입니다.

api와 notes는 Django project의 폴더이며, examples는 REST API에 데이터를 요청할 때 사용하는 방법의 예시입니다.


## Django REST API 예시 작동 방법
- Django 를 설치합니다. 명령어는 `pip install django==2.1.8`을 권장합니다.
- `pip install djangorestframework` 와 `pip install django-cors-headers`를 설치합니다.
- `python manage.py makemigrations`를 입력하고 `python manage.py migrate`를 입력해야 데이터 모델을 생성하고 사용할 수 있습니다.
- 서버를 실행시킵니다. `python manage.py runserver $IP:$PORT`
- server 주소에 더해서 /api/v1/memos/ 을 입력하면 구성된 API 화면을 확인할 수 있습니다. ex) http://0.0.0.0:8080/api/v1/memos


### REST API 요청 방법
- 원하는 페이지 (examples의 index.html 부분을 로컬에서 작동해도 확인할 수 있습니다) 에서 자바스크립트 ajax 콜을 이용해서 내용을 불러오거나 새 글을 추가할 수 있습니다.
- 아래 예시는 axios 패키지를 활용한 예시입니다.



```
생략
post 방식으로 요청을 보내는 예시
axios.post(this.url, { content: this.content }) // 첫 번째 인자는 URL 주소, 두번째 인자는 { 들어갈 데이터 } 입니다. 현재 models.py에서 content = models.TextField()로 정의했기 때문에 {content:}으로 지정했습니다.
          .then(response => { // 이후 원하는 동작을 적어주면 됩니다.
            this.getMemos()
            this.content = ''
          })
생략
axios.get(this.url) // get은 단순히 URL 주소만 요청하면 됩니다.
          .then(response => {
            this.memos = response.data
          })
생략
```



