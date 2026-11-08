## Create Project
create an virtual environment using -m venv <myProject>
activate it <myProject\Script\activate>
install django <pip install django>
create a django project <django-admin startproject my site>
<cd>change directory to my site
run django project<python manage.py runserver>

## Create an App
`python manage.py farm startapp fisrtApp`
`register the application in the main project`
        -navigate to project level settings.py

    '''
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstApp'
]
    '''
`add it to the path in the project evel urls`
        '''
        from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstApp/',include('firstApp.urls'))
]
        '''
`create a urls.py file inside  the firstApp application directory`
         '''
         from django.urls import path
from.import views #import views from the current root directory

urlpatterns = [
    path('produce' ,views.produceSector)
]

         '''

`Run it once more`

 python manage.py runserver

`Create a model`
-create a model class for('produce')

      '''
         # Create your models here.
class Produce(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    price = models.FloatField()
      '''

`make migration`  <python manage.py makemigrations>
`run a migration` <python manage.py migrate>

`Creat a superuser`
    -creat superuser<python manage.py createsuperuser>

`run`<python manage.py runserver>
navigate to /admin endpoint

`Register the model in the admin panel`
     <admin.site.register(models.produce)>

     '''     
from . import models
# Register your models here.

admin.site.register(models.Produce)

     '''

`Display data on template`
