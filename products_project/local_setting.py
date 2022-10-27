# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=gzhn5f3tp=fk(3k7@6vf(*oa=2*-povya!w-&c+f-y$(&zj7='

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password99!',
    }
}
