from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View


from timetable_tool.models import stations, train_records, stop_records, tickets, tickets_sold
from timetable_tool.forms import BuyForm, RouteForm, StationForm, TrainForm
from timetable_tool.utils import *

# TODO: active menu bar
# TODO: solve menu dropdown issue in Chrome
# TODO: auto complete
# TODO: unclear search

def index(request):
    return render(request, "index.html")

def route_search(request, route_input = None, date_input = None):
    if request.method == 'POST':
        route_form = RouteForm(request.POST)
        if(route_form.is_valid()):
            route_input = route_form.cleaned_data['route_input']
            date_input = route_form.cleaned_data['date_input']
        else:
            messages.error(request, "Error: Invalid form input")
            context = {"route_form": route_form} 
            return render(request, "route_search.html", context)
    else:
        route_form = RouteForm()
        if route_input and date_input and valid_route(route_input) and valid_date(date_input):
            route_input = replace_to_dash(route_input)
        else:
            if route_input or date_input:
                messages.error(request, "Error: Invalid input")
            context = {"route_form": route_form}
            return render(request, "route_search.html", context)
    
    stops = get_route_query(route_input, date_input)
    context = {"route_input": route_input, "date_input": date_input, \
                "stops": stops, "route_form": route_form}
    
    return render(request, "route_search.html", context)

    
def station_search(request, station_input = None, date_input = None):
    if request.method == 'POST':
        station_form = StationForm(request.POST)
        if(station_form.is_valid()):
            station_input = station_form.cleaned_data['station_input']
            date_input = station_form.cleaned_data['date_input']
        else:
            messages.error(request, "Error: Invalid form input")
            context = {"station_form": station_form} 
            return render(request, "station_search.html", context)
    else:
        station_form = StationForm()
        if not station_input or not date_input \
            or not valid_station(station_input) or not valid_date(date_input):
            if(station_input or date_input):
                messages.error(request, "Error: Invalid input")
            context = {"station_form": station_form}
            return render(request, "station_search.html", context)

    routes = get_station_query(station_input, date_input)
    context = {"station_input": station_input, "date_input": date_input, \
            "routes": routes, "station_form": station_form}
    
    return render(request, "station_search.html", context)


def train_search(request, depart_input = None, dest_input = None, date_input = None):
    if request.method == 'POST':
        train_form = TrainForm(request.POST)
        if(train_form.is_valid()):
            depart_input = train_form.cleaned_data['depart_input']
            dest_input = train_form.cleaned_data['dest_input']
            date_input = train_form.cleaned_data['date_input']
        else:
            messages.error(request, "Error: Invalid form input")
            context = {"train_form": train_form} 
            return render(request, "train_search.html", context)
    else:
        train_form = TrainForm()
        context = {"train_form": train_form}
        if not depart_input or not dest_input or not date_input \
            or not valid_station(depart_input) or not valid_station(dest_input) \
            or not valid_date(date_input):
            if(depart_input or dest_input or date_input):
                messages.error(request, "Error: Invalid input")
            context = {"train_form": train_form}
            return render(request, "train_search.html", context)

    trains = get_train_query(depart_input, dest_input, date_input)
    context = {"depart_input": depart_input, "dest_input": dest_input, \
            "date_input": date_input, "trains": trains, "train_form": train_form}
    
    return render(request, "train_search.html", context)


class TicketListView(LoginRequiredMixin, View):
    template = 'ticket_list.html'  # 'order_system.html'
    def get(self,request):
        context = {}
        return render(request, self.template, context=context)
    
    def post(self, request):
        # context = {}
        #if request.POST.get('submit') == 'submit':
        user_tickets = get_ticket_bought(self.request.user.id)
        context = {"tickets": user_tickets}
        return render(request, self.template, context=context)


class TicketBuyView(LoginRequiredMixin, View):
    template = 'ticket_buy.html'
    
    def get(self, request, pk_from, pk_to, pk_date) :
        form = BuyForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk_from, pk_to, pk_date) :
        form = BuyForm(request.POST)
        '''
        if not form.is_valid() :
            print("Form not valid!")
            messages.error(request, "Form not valid!")
            return render(request, self.template, ctx)
        '''
        ctx = {'form' : form}
            
        
        if not tickets.objects.filter(stop_from_id = pk_from, \
                    stop_to_id = pk_to, train_date = pk_date): 
            messages.error(request, "No tickets are sold!")
        else:
            tickets_all = tickets.objects.get(stop_from_id = pk_from, \
                    stop_to_id = pk_to, train_date = pk_date)
            if tickets_sold.objects.filter(ticket_id = tickets_all.id, \
                    customer_id = self.request.user.id):
                messages.error(request, "You have bought this ticket!")
            elif(int(request.POST['quantity']) > tickets_all.tickets_avaliable):
                messages.error(request, "Tickets are not enough!")
            else:
                messages.success(request, "Success!")
                # Add owner to the model before saving
                ticket_sold = form.save(commit=False)
                ticket_sold.customer = self.request.user
                ticket_sold.ticket_id = tickets_all.id
                ticket_sold.seat_number = tickets_all.tickets_avaliable
                ticket_sold.save()
                # update tickets avaliable
                tickets_all.tickets_avaliable -= int(request.POST['quantity'])
                tickets_all.save()
                return redirect(reverse_lazy('timetable_tool:ticket_all'))
        return redirect(reverse_lazy('timetable_tool:train_search'))


class TicketCancelView(LoginRequiredMixin, View):
    template = "ticket_cancel.html"
    def get(self, request, pk_tks):
        context = {}
        return render(request, self.template, context)
    
    def post(self, request, pk_tks):
        if "cancel" in request.POST:
            messages.info(request, "Ticket isn't cancelled!")
            return redirect(reverse_lazy('timetable_tool:ticket_all'))
        if not tickets_sold.objects.filter(id = pk_tks, \
            customer_id = self.request.user.id):
            messages.error(request, "Ticket doesn't exist!")
        else:
            ticket_cancel = tickets_sold.objects.get(id = pk_tks, \
                        customer_id = self.request.user.id)
            print(ticket_cancel.ticket_id)
            if not tickets.objects.filter(id = ticket_cancel.ticket_id):
                messages.error(request, "Ticket doesn't exist!")
            else:
                tickets_all = tickets.objects.get(id = ticket_cancel.ticket_id)
                tickets_all.tickets_avaliable += ticket_cancel.quantity
                tickets_all.save()
                ticket_cancel.delete()
                messages.success(request, "Ticket is cancelled successfully!")

        return redirect(reverse_lazy('timetable_tool:ticket_all'))
            