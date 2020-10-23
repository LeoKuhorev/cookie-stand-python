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
[Chuck Li  ](https://github.com/ticochuck)
[Richard Whitehead]()

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
`DB_NAME=azjzmpcc`  
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
`sales/` - sales page, shows the sales data information and historical data for the last two years (login required);
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

python = "^3.8"
django = "^3.1.2"
psycopg2-binary = "^2.8.6"
django-environ = "^0.4.5"
django-crispy-forms = "^1.9.2"
pillow = "^8.0.0"
django-cleanup = "^5.1.0"


### Dev Dependencies:

[Pylint-Django (v. 2.3.0)](https://pypi.org/project/pylint-django/)
