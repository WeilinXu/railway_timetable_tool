from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.urls import reverse_lazy

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations

class HomeView(View):
    def get(self, request) :
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed' : settings.INSTALLED_APPS,
            'islocal' : islocal
        }
        return render(request, 'home/main.html', context)

from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        # return redirect("/timetable_tool")
        return redirect(reverse_lazy('login'))
    else:
	    form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})

