DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-4qvb)whpmo%)d7c*#s9@5*n@@ac3p1oa+8x(cbi#%cvtglcxf6'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stepik_qa',
        'USER': 'postgres',
        'PASSWORD': '3329',
        'HOST': 'localhost',
        'PORT': '5433'
    },
}