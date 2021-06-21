from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from App_Event.forms import CreateEventSubmit
from django.conf import settings
from App_Account.models import Organization
from App_Event.models import Event, Donation
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
User = get_user_model()

# Create your views here.

def Home(request):

    return render(request, 'App_Event/home.html')

def Contactus(request):

    return render(request, 'App_Event/contactus.html')

def Eventdetails(request, slug):

    eventdetails = get_object_or_404(Event, slug=slug)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        hide_identity = request.POST.get('hide_identity')
        if request.user.is_authenticated:
            name = request.user.first_name
            email = request.user.email
            donations = Donation(user=request.user, event=eventdetails,  name=name, email=email, amount=amount)
            if hide_identity == 'True':
                donations.hide_identity = True
            donations.save()
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            donations = Donation(name=name, event=eventdetails, email=email, amount=amount)
            if hide_identity == 'True':
                donations.hide_identity = True
            donations.save()
    context = {
        'eventdetails': eventdetails
    }

    return render(request, 'App_Event/eventDetails.html', context)

def OrgApplyevent(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    if request.method == 'POST':
        form = CreateEventSubmit(request.POST or None, request.FILES or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = user
            event.save()
            return redirect('App_Organization:OrganizationDashboard', slug)
    else:
        form = CreateEventSubmit()
    context = {
        'form': form,
        'user': user,
        'org': org
    }


    return render(request, 'App_Organization/applyevent.html', context)

def OrgEventList(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    events = Event.objects.filter(user = org.org)
    print(events)
    context = {
        'user': user,
        'org': org,
        'events': events,
    }


    return render(request, 'App_Organization/orgeventlist.html', context)
