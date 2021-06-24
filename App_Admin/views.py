from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization, VerifyOrgBankDetails
from App_Event.models import Event, Donation
from App_Admin.forms import OrganizationConfirm
from App_Admin.eventdetailsforms import EventDetailsFromAdmin
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

def BannedOrganizationlist(request):

    organizations = Organization.objects.filter(banned=True)

    context = {
        'organizations': organizations
    }
    return render (request,'App_Admin/Organization/bannedorganization.html', context)

def UnverifiedOrganizationlist(request):

    organizations = Organization.objects.filter(is_verified=False)

    context = {
        'organizations': organizations
    }
    return render (request,'App_Admin/Organization/newunverifiedorganizations.html', context)

def OrganizationDetails(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    bankinfo = get_object_or_404(VerifyOrgBankDetails, user=user)

    if request.method == "POST":
        form = OrganizationConfirm(request.POST or None, instance=org)
        if form.is_valid():
            form.save()
            return redirect('App_Admin:organizationlist')

    form = OrganizationConfirm(instance=org)
    context = {
        'org': org,
        'bankinfo': bankinfo,
        'form': form
    }
    return render (request,'App_Admin/Organization/organizationdetails.html', context)

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

def EventDetails(request, slug):

    event = get_object_or_404(Event, slug=slug)

    if request.method == 'POST':
        form = EventDetailsFromAdmin(request.POST or None, instance=event)
        if form.is_valid():
            form.save()
            return redirect('App_Admin:eventlist')

    form = EventDetailsFromAdmin(instance=event)
    context = {
        'event': event,
        'form': form
    }
    return render (request,'App_Admin/Event/eventdetails.html', context)


def AllUsers(request):

    user = User.objects.all()

    context = {
        'user': user
    }
    return render (request,'App_Admin/User/alluser.html', context)


def UserDetails(request, pk):

    user = get_object_or_404(User, pk=pk)

    context = {
        'user': user
    }

    return render (request,'App_Admin/User/userdetails.html', context)

def LatestDonars(request):

    donars = Donation.objects.filter(ordered=True).order_by('date')

    context = {
        'donars': donars,
    }

    return render (request,'App_Admin/Donation/latestdonatios.html', context)

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
