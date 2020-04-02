from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages

from timetable_tool.models import stations, train_records, stop_records
from timetable_tool.execute_sql import *

# TODO: false redirect method

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def route_search(request, route_input = None, date_input = None):
    if request.method == 'POST':
        route_input = request.POST['route']
        date_input = request.POST['date']
    context = {}
    if route_input is not None and date_input is not None:
        if not valid_route(route_input) or \
                not valid_date(date_input):
            messages.error(request, "Error: Invalid input")
        else:
            route_input = replace_to_dash(route_input)
            stops = get_route_query(route_input, date_input)
            context = {"route_input": route_input, "date_input": date_input, "stops": stops}
    
    return render(request, "route_search.html", context)


def station_search(request, station_input = None, date_input = None):
    if request.method == 'POST':
        station_input = request.POST['station']
        date_input = request.POST['date']
    context = {}
    if station_input is not None and date_input is not None:
        if not valid_station(station_input) or \
                not valid_date(date_input):
            messages.error(request, "Error: Invalid input")
        else:
            routes = get_station_query(station_input, date_input)
            context = {"station_input": station_input, "date_input": date_input, "routes": routes}
    
    return render(request, "station_search.html", context)


def train_search(request, depart_input = None, dest_input = None, date_input = None):
    if request.method == 'POST':
        depart_input = request.POST['station_depart']
        dest_input = request.POST['station_dest']
        date_input = request.POST['date']
    context = {}
    if depart_input is not None and dest_input is not None and date_input is not None:
        if not valid_station(depart_input) or \
            not valid_station(dest_input) or \
            not valid_date(date_input):
            messages.error(request, "Error: Invalid input")
        else:
            # Query database
            trains = get_train_query(depart_input, dest_input, date_input)
            context = {"depart_input": depart_input, "dest_input": dest_input, "date_input": date_input, "trains": trains}
    
    return render(request, "train_search.html", context)