from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from . import views as v # newly added

urlpatterns = [
    path('', views.HomeView.as_view(),name='index'),
    path("register/", v.register, name="register"),  # newly added
]

