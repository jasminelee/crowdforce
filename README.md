Crowdforce
==========

Crowdforce Django App

Installing Dependencies
==

Dependencies are listed in requirements.txt. If you use a module that is not in the list, simply add it to the list before the next commit. To get the exact version number, run:
```
pip freeze | grep [module name]
```

Using Virtualenv *(recommended)*
--

First, install virtualenv (http://pypi.python.org/pypi/virtualenv)

Create a new virtual environment for the project. This makes deployments more consistent.
```
$ virtualenv venv --distribute
```

Start using the new Virtualenv:
```
$ source venv/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Run the server
==

CD to the root of the repo, then type:
```
$ python manage.py runserver
```

Get DB running
==

**The choice of local db is yours.**

* There is a file called local_settings.py.default.
* Copy this file and rename it to local_settings.py.
* You can then add whatever database settings you like, but those there are my personal settings, using postgres.
* Assuming you only models to write queries, database choice does not matter for development.

*In deployment, we'll use Heroku's specially flavored PostgreSQL.*
