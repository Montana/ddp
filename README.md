# Docker-Prowl


This is simple Django production ready Docker container for Prowl. It contains nginx+gunicorn serving static content and running a WSGI server for the Django project in question, managed by supervisord.

By default this machine will create a container listening on all interfaces on port 8001. The container will be called 'django_app'.


## Usage example

<pre>
mkdir django-prod
cd django-prod
git init
git remote add upstream https://github.com/Montana/docker-django-prowl
git pull upstream master
make create
</pre>

## Using it with MySQL

<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_ENV_MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_ENV_MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_ENV_MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_PORT_3306_TCP_ADDR'),
        'PORT': os.environ.get('MYSQL_PORT_3306_TCP_PORT'),
    }
}
</pre>

To export needed env variables, you need to define the env file. For development simply add needed env variables in your env file in root. This is all you need to do. 

Actually there are MySQL/PostgreSQL settings that comment out in that file already, just make them work for your machine.

Written by Montana Mendy.
