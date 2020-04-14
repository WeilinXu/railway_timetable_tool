from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.db.models import Q

from django.utils.translation import ugettext_lazy as _

from timetable_tool.models import stations, train_records, stop_records, tickets, tickets_sold
from timetable_tool.forms import RouteForm, StationForm, TrainForm
from timetable_tool.utils import *

# TODO: active menu bar
## TODO: / to %2F in url
## TODO: consider date in search (not assume run every day)

def index(request):
    return render(request, "index.html")

def route_search(request, route_input = None, date_input = None):
    if request.method == 'GET':
        route_form = RouteForm()
        context = {"route_form": route_form}
        strval =  request.GET.get("submit", False)
        if strval:
            route_form = RouteForm(request.GET)
            if(route_form.is_valid()):
                route_input = route_form.cleaned_data['route_input']
                date_input = route_form.cleaned_data['date_input']
            else:
                messages.error(request, _("Error: Invalid form input"))
                return render(request, "route_search.html", context)
        elif(route_input or date_input):
            if route_input and date_input  \
                and valid_route(route_input) and valid_date(date_input):
                route_input = replace_to_dash(route_input)
            else:
                messages.error(request, _("Error: Invalid input"))
                return render(request, "route_search.html", context)
        else:
            return render(request, "route_search.html", context)
        
        stops = get_route_query(route_input, date_input)
        context = {"route_input": route_input, "date_input": date_input, \
                    "stops": stops, "route_form": route_form}
        return render(request, "route_search.html", context)

    
def station_search(request, station_input = None, date_input = None):
    if request.method == 'GET':
        station_form = StationForm()
        context = {"station_form": station_form}

        strval =  request.GET.get("submit", False)
        if strval:
            station_form = StationForm(request.GET)
            if(station_form.is_valid()):
                station_input = station_form.cleaned_data['station_input']
                date_input = station_form.cleaned_data['date_input']
            else:
                messages.error(request, _("Error: Invalid form input"))
                return render(request, "station_search.html", context)
        elif(station_input or date_input):
            if not station_input or not date_input \
                or not valid_station(station_input) or not valid_date(date_input):
                messages.error(request, _("Error: Invalid input"))
                return render(request, "station_search.html", context)
        else:
            return render(request, "station_search.html", context)
        
        routes = get_station_query(station_input, date_input)
        context = {"date_input": date_input, \
                "routes": routes, "station_form": station_form}
        context["station_input"], context[ "station_input_cn"] \
            = get_station_names(station_input)
        return render(request, "station_search.html", context)


def train_search(request, depart_input = None, dest_input = None, date_input = None):
    if request.method == 'GET':
        train_form = TrainForm()
        context = {"train_form": train_form}
        strval =  request.GET.get("submit", False)
        if strval:
            train_form = TrainForm(request.GET)
            if(train_form.is_valid()):
                depart_input = train_form.cleaned_data['depart_input']
                dest_input = train_form.cleaned_data['dest_input']
                date_input = train_form.cleaned_data['date_input']
            else:
                messages.error(request, _("Error: Invalid form input"))
                return render(request, "train_search.html", context)
        elif(depart_input or dest_input or date_input):
            print("3")
            if not depart_input or not dest_input or not date_input \
                or not valid_station(depart_input) or not valid_station(dest_input) \
                or not valid_date(date_input):
                if(depart_input or dest_input or date_input):
                    messages.error(request, _("Error: Invalid input"))
                
                return render(request, "train_search.html", context)
        else:
            return render(request, "train_search.html", context)
        
        trains = get_train_query(depart_input, dest_input, date_input)
        context = {"date_input": date_input, \
                "trains": trains, "train_form": train_form}
        context["depart_input"], context[ "depart_input_cn"] \
            = get_station_names(depart_input)
        context["dest_input"], context[ "dest_input_cn"] \
            = get_station_names(dest_input)
        return render(request, "train_search.html", context)

class TicketListView(LoginRequiredMixin, View):
    template = 'ticket_list.html'  # 'order_system.html'
    
    def get(self,request):
        strval1 =  request.GET.get("future", False)
        if strval1:
            user_tickets = get_ticket_bought(self.request.user.id, 'future')
            can_cancel = True
        else:
            strval2 =  request.GET.get("history", False)
            if strval2:
                user_tickets = get_ticket_bought(self.request.user.id, 'history')
                can_cancel = False
            else:
                context = {"empty_form": True}
                return render(request, self.template, context=context)
        
        request.session['my_tickets'] = {}
        for user_ticket in user_tickets:
            request.session['my_tickets'][user_ticket["ticket_id"]] = \
                    {"station_from": user_ticket["station_from"], \
                    "station_to": user_ticket["station_to"], \
                    "station_from_cn": user_ticket["station_from_cn"], \
                    "station_to_cn": user_ticket["station_to_cn"], \
                    "train_number": user_ticket["train_number"], \
                    "depart_date": str(user_ticket["train_date"]), \
                    "depart_time": str(user_ticket['dep_time']),\
                    "price": user_ticket['price'],\
                    "quantity": user_ticket['quantity'],}
        context = {"tickets": user_tickets, "can_cancel": can_cancel}
        return render(request, self.template, context=context)
                

class TicketBuyView(LoginRequiredMixin, View):
    template = 'ticket_buy.html'
    def get(self, request, pk_from, pk_to, pk_date):
        dep_info = get_stop_record_info(pk_from, is_arr = False)
        arr_info = get_stop_record_info(pk_to, is_arr = True)
        dep_date = datetime.datetime.strptime(pk_date, '%Y-%m-%d')
        arr_date, _ = get_arr_date(dep_info['stop_day'], dep_date, arr_info['stop_day'])
        price = get_price(arr_info['km'] - dep_info['km'])
        request.session['current_price'] = price
        ctx = {'dep_info': dep_info, 'dep_date': dep_date, \
                'arr_info': arr_info, 'arr_date': arr_date, 'price': price}
        return render(request, self.template, ctx)

    def post(self, request, pk_from, pk_to, pk_date) :
        if not tickets.objects.filter(stop_from_id = pk_from, \
                    stop_to_id = pk_to, train_date = pk_date): 
            messages.error(request, _("No tickets are sold!"))
        else:
            tickets_all = tickets.objects.get(stop_from_id = pk_from, \
                    stop_to_id = pk_to, train_date = pk_date)
            if tickets_sold.objects.filter(ticket_id = tickets_all.id, \
                    customer_id = self.request.user.id):
                messages.error(request, _("You have bought this ticket!"))
            elif(int(request.POST['quantity']) > tickets_all.tickets_avaliable):
                messages.error(request, _("Tickets are not enough!"))
            else:
                messages.success(request, _("Success!"))
                # Add owner to the model before saving
                quantity_in = int(request.POST['quantity'])
                ticket_sold = tickets_sold(customer = self.request.user, \
                                ticket_id = tickets_all.id, \
                                seat_number = tickets_all.tickets_avaliable, \
                                quantity = quantity_in, \
                                price = request.session['current_price'] * quantity_in)
                ticket_sold.save()
                # update tickets avaliable
                tickets_all.tickets_avaliable -= quantity_in
                tickets_all.save()
                return redirect(reverse_lazy('timetable_tool:ticket_all'))
        return redirect(reverse_lazy('timetable_tool:train_search'))


class TicketCancelView(LoginRequiredMixin, View):
    template = "ticket_cancel.html"
    def get(self, request, pk_tks):
        if str(pk_tks) in request.session['my_tickets']:
            temp_data = request.session['my_tickets'][str(pk_tks)]
            context = {"ticket_info": temp_data}
        return render(request, self.template, context)
    
    def post(self, request, pk_tks):
        if "cancel" in request.POST:
            messages.info(request, _("Ticket isn't refunded!"))
            return redirect(reverse_lazy('timetable_tool:ticket_all'))
        if not tickets_sold.objects.filter(id = pk_tks, \
            customer_id = self.request.user.id):
            messages.error(request, _("Ticket doesn't exist!"))
        else:
            ticket_cancel = tickets_sold.objects.get(id = pk_tks, \
                        customer_id = self.request.user.id)
            print(ticket_cancel.ticket_id)
            if not tickets.objects.filter(id = ticket_cancel.ticket_id):
                messages.error(request, _("Ticket doesn't exist!"))
            else:
                tickets_all = tickets.objects.get(id = ticket_cancel.ticket_id)
                if can_cancel(request.session['my_tickets'], pk_tks):
                    tickets_all.tickets_avaliable += ticket_cancel.quantity
                    money_return = ticket_cancel.price
                    tickets_all.save()
                    ticket_cancel.delete()
                    messages.success(request, _("Ticket is cancelled successfully and %(money)s Yuan will return to your account!") % {'money': str(money_return)})
                else:
                    messages.error(request, _("Past Ticket cannont be cancelled!"))
        return redirect(reverse_lazy('timetable_tool:ticket_all'))
            

def station_autocomplete(request):  # get_town
    if request.is_ajax():
        q = request.GET.get('term', '')
        results = []
        if(is_cn()):
            print("enter")
            stations_down = stations.objects.filter(Q(station_name_cn__startswith = q))
            for station_down in stations_down:
                name_json = station_down.station_name_cn   # name
                results.append(name_json)
        else:
            stations_down = stations.objects.filter(Q(station_name__startswith = q))
            for station_down in stations_down:
                name_json = station_down.station_name   # name
                results.append(name_json)
        data = {'result_list': results}
        return JsonResponse(data)

def route_autocomplete(request):  # get_town
    if request.is_ajax():
        q = request.GET.get('term', '')
        routes_down = train_records.objects.filter(Q(train_number__startswith = q))
        results = []
        for route_down in routes_down:
            name_json = route_down.train_number   # name
            results.append(name_json)
        data = {'result_list': results}
        return JsonResponse(data)