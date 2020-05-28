from django.shortcuts import render
from .models import Airport,Airline,Route


def airport(request):
    airport = Airport.objects.all()
    return render(request, "airport.html", {"airport": airport})

def airline(request, id):
    airline = Airline.objects.filter(airportID=id)
    airport = Airport.objects.get(id=id)
    return render(request, "airline.html", {"airline": airline, "airport": airport})

def route(request, id):
    route = Route.objects.filter(airlineID=id)
    airline = Airline.objects.get(id=id)
    return render(request, "route.html", {"route": route, "airline": airline})