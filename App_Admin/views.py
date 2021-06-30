from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from App_Account.models import Organization, VerifyOrgBankDetails, VerifyPersonBankDetails, Profile
from datetime import datetime
from App_Event.models import Event, Donation, Withdraw
from App_Event.forms import WithdrawConfirm
from App_Admin.forms import OrganizationConfirm
from App_Admin.eventdetailsforms import EventDetailsFromAdmin, VerifyPerson
from decimal import Decimal
from django.db.models import Q
User = get_user_model()

# Create your views here.
# def master(request):
#     return render(request,'App_Admin/master.html')

@login_required(login_url = '/login/')
def Home(request):
    if request.user.is_staff:
        transection = Donation.objects.filter(date__gte = datetime.now().replace(hour=0,minute=0,second=0))
        totalevents = Event.objects.all().count()
        events = Event.objects.filter(endtime__gt = datetime.now().replace(hour=0,minute=0,second=0)).count()
        users = User.objects.filter(is_active=True).count()
        totalorg = User.objects.filter(is_org=True).count()
        verifiedorg = Organization.objects.filter(is_verified=True).count()
        staffs = User.objects.filter(is_staff=True).count()
        verifiedPerson = User.objects.filter(is_personorg=True).count()
        totaltrans = 0
        for trans in transection:
            totaltrans += Decimal(trans.amount)
        print(staffs)
        context = {
            'totaltrans': totaltrans,
            'users': users,
            'totalorg': totalorg,
            'verifiedorg': verifiedorg,
            'verifiedPerson': verifiedPerson,
            'totalevents': totalevents,
            'events': events,
            'staffs': staffs,
        }
        return render(request,'App_Admin/home.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Organizationlist(request):

    if request.user.is_staff:
        organizations = Organization.objects.all()

        context = {
            'organizations': organizations
        }
        return render (request,'App_Admin/Organization/organizationlist.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def BannedOrganizationlist(request):

    if request.user.is_staff:
        organizations = Organization.objects.filter(banned=True)

        context = {
            'organizations': organizations
        }
        return render (request,'App_Admin/Organization/bannedorganization.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UnverifiedOrganizationlist(request):

    if request.user.is_staff:
        organizations = Organization.objects.filter(is_verified=False)

        context = {
            'organizations': organizations
        }
        return render (request,'App_Admin/Organization/newunverifiedorganizations.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def OrganizationDetails(request, slug):

    if request.user.is_staff:
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
    else:
        return render(request, 'notauthorised.html')


@login_required(login_url = '/login/')
def Eventlist(request):

    if request.user.is_staff:
        event = Event.objects.filter(active=True)

        context = {
            'event': event
        }
        return render (request,'App_Admin/Event/eventslist.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UnverifiedEventlist(request):

    if request.user.is_staff:
        event = Event.objects.filter(active=False)

        context = {
            'event': event
        }
        return render (request,'App_Admin/Event/notverifiedeventslist.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def EventDetails(request, slug):

    if request.user.is_staff:
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
    else:
        return render(request, 'notauthorised.html')


@login_required(login_url = '/login/')
def AllUsers(request):

    if request.user.is_staff:
        user = User.objects.all()

        context = {
            'user': user
        }
        return render (request,'App_Admin/User/alluser.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def AllUsers(request):

    if request.user.is_staff:
        user = User.objects.all()

        context = {
            'user': user
        }
        return render (request,'App_Admin/User/alluser.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def VerifiedUsers(request):

    if request.user.is_staff:
        user = User.objects.filter(is_personorg=True)

        context = {
            'user': user
        }
        return render (request,'App_Admin/User/verifieduser.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UnVerifiedUsers(request):

    if request.user.is_staff:
        user = VerifyPersonBankDetails.objects.filter(filled=True, is_verified=False)
        print(user)
        context = {
            'user': user
        }
        return render (request,'App_Admin/User/unverifieduser.html', context)
    else:
        return render(request, 'notauthorised.html')


@login_required(login_url = '/login/')
def UnVerifiedUsersBankDetails(request, pk):

    if request.user.is_staff:
        user = get_object_or_404(VerifyPersonBankDetails, pk=pk)
        profile = get_object_or_404(Profile, user=user.user)

        if request.method == 'POST':
            form = VerifyPerson(request.POST or None, instance=user)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                return redirect('App_Admin:unverifiedusers')
        else:
            form = VerifyPerson(instance = user)
        context = {
            'user': user,
            'profile': profile,
            'form': form
        }
        return render (request,'App_Admin/User/unverifieduserbankdetails.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UserDetails(request, pk):

    if request.user.is_staff:
        user = get_object_or_404(User, pk=pk)

        context = {
            'user': user
        }

        return render (request,'App_Admin/User/userdetails.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def LatestDonars(request):

    donars = Donation.objects.filter(ordered=True).order_by('date')

    context = {
        'donars': donars,
    }

    return render (request,'App_Admin/Donation/latestdonatios.html', context)

@login_required(login_url = '/login/')
def PendingWithdraw(request):

    withdraw = Withdraw.objects.filter(confirm=False).order_by('date')

    context = {
        'withdraw': withdraw,
    }

    return render (request,'App_Admin/Withdwar/pendingwithdraw.html', context)

@login_required(login_url = '/login/')
def ConfirmWithdraw(request, pk):

    withdraw = get_object_or_404(Withdraw, pk=pk)

    if request.method == 'POST':
        form = WithdrawConfirm(request.POST or None, instance=withdraw)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('App_Admin:pendingwithdraw')
    else:
        form = WithdrawConfirm(instance=withdraw)

    context = {
        'withdraw': withdraw,
        'form':form
    }

    return render (request,'App_Admin/Withdwar/pendingwithdraw.html', context)

@login_required(login_url = '/login/')
def ReadytoWithdraw(request):

    withdraw = Withdraw.objects.filter(status=True, confirm=False).order_by('date')

    context = {
        'withdraw': withdraw,
    }

    return render (request,'App_Admin/Withdwar/readytowithdraw.html', context)

@login_required(login_url = '/login/')
def ConfirmReadytoWithdraw(request, pk):

    withdraw = get_object_or_404(Withdraw, pk=pk)

    if request.method == 'POST':
        form = WithdrawConfirm(request.POST or None, instance=withdraw)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('App_Admin:readytowithdraw')
    else:
        form = WithdrawConfirm(instance=withdraw)

    context = {
        'withdraw': withdraw,
        'form':form
    }

    return render (request,'App_Admin/Withdwar/confirmreadytowithdraw.html', context)

@login_required(login_url = '/login/')
def AllWithdrawDone(request):

    withdraw = Withdraw.objects.filter(status=True, confirm=True).order_by('date')

    context = {
        'withdraw': withdraw,
    }

    return render (request,'App_Admin/Withdwar/allwithdrawdone.html', context)



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
