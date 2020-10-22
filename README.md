# Lab-44 Salmon-Cookies

## Feature Tasks and Requirements

- create Django application from scratch that has a custom user model named CustomUser
  - Custom user should use email instead of username for signup / login
  - Application should work with Django Admin

## AUTHORS

[_Leo Kukharau_](https://github.com/LeoKuhorev)

## GETTING STARTED:

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py runserver` - to run server

### <a name="env"></a> ENV variables:

`SECRET_KEY=t9s9_g3j3(5ry#j=)ctik)i&(k%!sta*^gfyt5smt*s8o=32z9`  
`DEBUG=True`  
`ALLOWED_HOSTS=127.0.0.1,0.0.0.0,localhost`  
`DB_USER=azjzmpcc`  
`DB_PASS=neEI-JS6iOrYMblJNVH-IZ_T8TWCe_25`  
`DB_HOST=lallah.db.elephantsql.com`   
`DB_PORT=5432`

## API:

`/` - landing page;  
`user/register/` - register page, handles user registration;  
`user/login/` - login page, allows a user to log in;  
`user/profile/` - profile page, allows a user to view and edit their profile information (login required);  
`user/logout/` - logout page, is shown when a user it logged out (login required);  
`admin/` - site admin page;

   

## Testing Info

| Email             |  Password  |     Role |
| ----------------- | :--------: | -------: |
| admin@test.com    | test123456 |    admin |
| sam@test.com      | test123456 |  manager |
| amanda@test.com   | test123456 |  manager |
| brook@test.com    | test123456 |  manager |
| john@test.com     | test123456 |  manager |
| robin@test.com    | test123456 |  manager |
| jb@test.com       | test123456 |  manager |
| customer@test.com | test123456 | customer |

### Dependency Documentation:

[Python (v. 3.8)](https://docs.python.org/3.8/)  
[Django (v. 3.1)](https://docs.djangoproject.com/en/3.1/)  
[Django Crispy Forms (v. 1.9.2)](https://pypi.org/project/django-crispy-forms/)  
[Django Environ (v. 0.4.5)](https://pypi.org/project/django-environ/)

### Dev Dependencies:

[Pylint-Django (v. 2.3.0)](https://pypi.org/project/pylint-django/)
