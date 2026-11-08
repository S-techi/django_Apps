from django.urls import path
from . import views

urlpatterns = [
    path('name/',views.name),

    path('nav/',views.nav)
]
