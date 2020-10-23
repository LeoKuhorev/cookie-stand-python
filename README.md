# Lab-44 Salmon-Cookies

## Feature Tasks and Requirements

- Create Salmon Cookies using Python  
    - Need to implement database  
    - Admin needs the ability to see sales from all stores. Only the admin can add new stores.  
- Store managers can see all data but only modify their store data.  
- Users create an account to purchase cookies online
- When not logged in, user can only see main page with cookies, costs, and merchandise.  
- Must use pictures in assets folder. (Can use any additional pictures)
use your imagination . . . . . to do????  

- Use this data to generate 2 years of data for each store. As new information is generated, update average customers, average cookies sold, and average cookie sales for each store.


## AUTHORS

[_Leo Kukharau_](https://github.com/LeoKuhorev)  
Chuck Li  
Richard Whitehead

## GETTING STARTED:

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py runserver` - to run server

### <a name="env"></a> ENV variables:

SECRET_KEY=secret key for the app (typically 50-characters long string)  
DEBUG=should be set to True in development  
ALLOWED_HOSTS=localhost,127.0.0.1

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
