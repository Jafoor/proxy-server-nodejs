from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization
from App_Event.models import Event
User = get_user_model()

# Create your views here.
# def master(request):
#     return render(request,'App_Admin/master.html')

def Home(request):
    return render(request,'App_Admin/home.html')

def Organizationlist(request):

    organizations = Organization.objects.all()

    context = {
        'organizations': organizations
    }
    return render (request,'App_Admin/Organization/organizationlist.html', context)

def Eventlist(request):

    event = Event.objects.filter(active=True)

    context = {
        'event': event
    }
    return render (request,'App_Admin/Event/eventslist.html', context)

def UnverifiedEventlist(request):

    event = Event.objects.filter(active=False)

    context = {
        'event': event
    }
    return render (request,'App_Admin/Event/notverifiedeventslist.html', context)

def AllUsers(request):

    user = User.objects.all()

    context = {
        'user': user
    }
    return render (request,'App_Admin/User/alluser.html', context)

#
# def verifiedusers(request):
#     return render (request,'App_Admin/verifiedusers.html')
#
# def generalusers(request):
#     return render (request,'App_Admin/generalusers.html')
#
# def eventsbyusers(request):
#     return render (request,'App_Admin/eventsbyusers.html')
#
# def eventsbyorganizations(request):
#     return render (request,'App_Admin/eventsbyorganizations.html')
