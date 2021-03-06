# railway_timetable_tool

## Setup Environment
In `railway_timetable_tool/`:
```
python3 -m venv env
source env/bin/activate
pip install django
pip install -r requirements.txt
django-admin startproject mysite

```

## Write code
Refer to [DJ4E](https://www.dj4e.com/assn/dj4e_install.md) and [DJ4E_hello_world_assignment](https://www.dj4e.com/assn/dj4e_hello.md?PHPSESSID=e57e049f726e5f6ffa231212345a0eb6)

### Setup project 
In `railway_timetable_tool/`:
```
django-admin startproject mysite
chmod +x ./bin/timetabledb
chmod +x ./bin/timetablerun
```

As mentioned in reference, change the specific lines in file `railway_timetable_tool/mysite/mysite/settings.py` and `railway_timetable_tool/mysite/mysite/wsgi.py`.

### Setup html template and bootstrap
Refer to [Login / Autos CRUD](https://www.dj4e.com/assn/dj4e_autos.md?PHPSESSID=f20467a664b7c6f6b43c17cf4fed9d9b)
In `railway_timetable_tool/mysite/`:
```
python manage.py startapp home
```
Add files `railway_timetable_tool/mysite/home/templates/home/main.html`, `railway_timetable_tool/mysite/home/templates/registration/login.html`, `railway_timetable_tool/mysite/home/templates/base_bootstrap.html`, and `railway_timetable_tool/mysite/home/templates/base_menu.html`.

### Setup Login
In `railway_timetable_tool/mysite/`:
```
python manage.py createsuperuser
```

### Setup app
Refer to [django_tutorial3](https://docs.djangoproject.com/en/3.0/intro/tutorial03/)

In `railway_timetable_tool/mysite/`:
```
python manage.py startapp timetable_tool
```

Then, design the database model in `./railway_timetable_tool/model.py` and url in `railway_timetable_tool/mysite/urls.py`.

Write view in file `./railway_timetable_tool/view.py` and corresponding `.html` files in `./railway_timetable_tool/templates/railway_timetable_tool/`.

Afterwards, register the model in `./railway_timetable_tool/admin.py` and append lines in `./mysite/settings.py`, `./mysite/urls.py` and `./mysite/home/templates/home/main.html`.


Finally, (in `railway_timetable_tool/mysite/`) check errors by:
```
python manage.py check
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

and migrate data by:
```
python data_import.py
python manage.py makemigrations
python manage.py migrate
```

which can be simplified by (in `railway_timetable_tool`):
```
./bin/timetabledb reset
```
## Translation
Refer to [tutorial](https://www.jianshu.com/p/bc3ada1b2ba1) and [trouble-shooting](https://stackoverflow.com/questions/2328185/django-i18n-common-causes-for-translations-not-appearing):

Use `i18n_patterns` in `mysite/urls.py`.

In `mysite/settings.py`: 

add `'django.middleware.locale.LocaleMiddleware'` to `MIDDLEWARE`; add `LOCALE_PATHS`.

Run `python manage.py makemessages -l zh_Hans` in `railway_timetable_tool/` folder.

Then, the file `zh_Hans/LC_MESSAGES/django.po` are generated in `railway_timetable_tool/mysite/locale/` folder. Add translations in this file.

In folder `railway_timetable_tool/mysite`, run:
```
django-admin compilemessages
```

## Run
In `railway_timetable_tool/mysite/`:
```
python manage.py runserver
```
Or in `railway_timetable_tool`:
```
./bin/timetablerun
```

In browser, enter: <http://localhost:8000/timetable_tool/>

