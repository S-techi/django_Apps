from django.urls import path
from . import views #import views from the current root directory

urlpatterns = [
    path('produceSector' ,views.produceSector),
    path('greeting',views.greeting),
    path('name',views.name)
]