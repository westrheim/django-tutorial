# django-tutorial
Just trying to get used to stuff by implementing this https://docs.djangoproject.com/en/3.0/intro/tutorial01/



# Terminal commands step-by step

```bash
python -m venv venv
source venv/bin/activate
python -m pip install django
python -m django --version
python -m pip install --upgrade pip

django-admin startproject mysite
cd mysite
python manage.py runserver
python manage.py startapp polls

python manage.py migrate

# Added models for Polls. Create migrations
python manage.py makemigrations polls
# Can see the migrations (in sql queries):
python manage.py sqlmigrate polls 0001
# Can also run this to check that everything is ok
python manage.py check

# Apply migrations
python manage.py migrate

# Invoke the python shell (with references to the settings module)
python manage.py shell

# Create admin users
python manage.py createsuperuser

```

# Takeaways
For your next project, remember to load secret keys from environment variables. Could do so the following way: 
* create two files (`.env.example` and `.env`).
* put the secrets into the `.env` file (and the same without the secrets in `.env.example`). The file could look like this
```
DJANGO_SECRET_KEY=lelelelelllefalkjnflkaejnfie
```
* Add the following code to the django settings module:
```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
```