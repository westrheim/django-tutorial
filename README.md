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

# Run tests for app
python manage.py test polls

```

# Takeaways
Some notes i wrote along the project

## Security
For your next project, remember to load secret keys from environment variables. Could do so the following way: 
* create two files (`.env.example` and `.env`).
* put the secrets into the `.env` file (and the same without the explicit secrets in `.env.example`). The file could lolike thisok 
```
# .env example
DJANGO_SECRET_KEY=lelelelelllefalkjnflkaejnfie
```
* Add the following code to the django settings module:
```python
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
```
This link could be relevant to revisit:
[How To Harden the Security of Your Production Django Project](https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project)


## Generic Views
There are two generic views in Django that can be used (to remove unneccessary code):

*DetailView*:
* Used for creating detail pages (like the page for a product)
* Specify which model to use by setting `model = Question`
* Specify what template to use by setting `template = ...` (defaults to `templates/<app>/<model>_detail.html`)
* Inside the template file, the model object context can be referenced to as `object`
* Other context could be created and added by using the get_context_data function


*ListView*:
* Used for creating list-based pages (like the list of products)
* Usually fetched from a queryset (like selecting a subset of products)
* Same as before with the templates (defaults to `templates/<app>/<model>_list.html`)
* Inside the template file, the model object context can be referenced to as `object_list`
* If something else than the model is going to be used in the template (for instance data from a queryset), `context_object_name` needs to be specified
