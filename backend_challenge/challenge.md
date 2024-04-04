<!-- before starting you must have a 
Python  version > 3.11.0 -->
cd .\backend_challenge\


pip install -r .\requirements.txt

python manage.py makemigrations

python manage.py migrate


python manage.py shell

from django.contrib.auth.models import User
<!-- these user are dummy users you can create your desired user
  -->
user1 = User.objects.create_user(username='user1', password='password1', is_staff=True)
user2 = User.objects.create_user(username='user2', password='password2', is_staff=True)



python manage.py runserver


1 : Now  in Postman:  access this url using Post method (http://127.0.0.1:8000/api/token/) with body of { "username":"user1",
"password":"password1"}

2: this will give you response of refresh and access token 
3:  Authorization in Headers likewise( Authorization : Bearer ################token-here#########)
     Now use the access token in body for CRUD.
     http://127.0.0.1:8000/api/tasks/
     http://127.0.0.1:8000/api/tasks/<int:pk>/

     http://127.0.0.1:8000/api/labels/
     http://127.0.0.1:8000/api/labels/<int:pk>/






