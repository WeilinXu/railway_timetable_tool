from django.urls import path
from . import views

app_name = 'timetable_tool'
urlpatterns = [
    path('', views.index, name='index'),
    path('routesearch/', views.route_search, name='route_search'),
    path('routesearch/<route_input>/<date_input>/', views.route_search, name='route_search2'),
    path('stationsearch/', views.station_search, name='station_search'),
    path('stationsearch/<station_input>/<str:date_input>/', views.station_search, name='station_search2'),
    path('trainsearch/', views.train_search, name='train_search'),
    path('trainsearch/<depart_input>/<dest_input>/<str:date_input>/', views.train_search, name='train_search2'),
]