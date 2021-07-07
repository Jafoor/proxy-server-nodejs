from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from App_Account.models import Organization, VerifyOrgBankDetails, VerifyPersonBankDetails, Profile
from datetime import datetime
from App_Event.models import Event, Donation, Withdraw
from App_Admin.models import Issue, Contactus, SupportedBanks
from App_Event.forms import WithdrawConfirm
from App_Admin.forms import OrganizationConfirm , IssueConfirm, ContactusDetails
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
        verifypersonbankdetails = get_object_or_404(VerifyPersonBankDetails, pk=pk)
        profile = get_object_or_404(Profile, user=verifypersonbankdetails.user)

        if request.method == 'POST':
            form = VerifyPerson(request.POST or None, instance=verifypersonbankdetails)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                if verifypersonbankdetails.is_verified == True:
                    user = request.user
                    user.is_personorg = True
                    user.save()

                return redirect('App_Admin:unverifiedusers')
        else:
            form = VerifyPerson(instance = verifypersonbankdetails)
        context = {
            'user': verifypersonbankdetails,
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

    if request.user.is_staff:
        donars = Donation.objects.filter(ordered=True).order_by('date')

        context = {
            'donars': donars,
        }

        return render (request,'App_Admin/Donation/latestdonatios.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def PendingWithdraw(request):

    if request.user.is_staff:
        withdraw = Withdraw.objects.filter(confirm=False).order_by('date')

        context = {
            'withdraw': withdraw,
        }

        return render (request,'App_Admin/Withdwar/pendingwithdraw.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def ConfirmWithdraw(request, pk):

    if request.user.is_staff:
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
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def ReadytoWithdraw(request):

    if request.user.is_staff:

        withdraw = Withdraw.objects.filter(status=True, confirm=False).order_by('date')

        context = {
            'withdraw': withdraw,
        }

        return render (request,'App_Admin/Withdwar/readytowithdraw.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def ConfirmReadytoWithdraw(request, pk):

    if request.user.is_staff:
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
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def AllWithdrawDone(request):

    if request.user.is_staff:
        withdraw = Withdraw.objects.filter(status=True, confirm=True).order_by('date')

        context = {
            'withdraw': withdraw,
        }

        return render (request,'App_Admin/Withdwar/allwithdrawdone.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Issues(request):

    if request.user.is_staff:
        issue = Issue.objects.filter(solved=True).order_by('date')

        context = {
            'issue': issue,
        }
        return render(request, 'App_Admin/Issue/solvedissue.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Issuedetails(request, pk):

    if request.user.is_staff:
        issue = get_object_or_404(Issue, pk=pk)
        if request.method == 'POST':
            form = IssueConfirm(request.POST or None, instance=issue)
            if form.is_valid():
                f = form.save(commit=False)
                f.save()
                return redirect('App_Admin:solvedissues')
        else:
            form = IssueConfirm(instance=issue)

        context = {
            'issue': issue,
            'form':form
        }
        return render(request, 'App_Admin/Issue/issuedetails.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Issuesread(request):

    if request.user.is_staff:
        issue = Issue.objects.filter(read=True, solved=False).order_by('date')

        context = {
            'issue': issue,
        }
        return render(request, 'App_Admin/Issue/issueread.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Issueworkingon(request):

    if request.user.is_staff:
        issue = Issue.objects.filter(status=True, solved=False).order_by('date')

        context = {
            'issue': issue,
        }
        return render(request, 'App_Admin/Issue/issueworkingon.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Issuenew(request):

    if request.user.is_staff:
        issue = Issue.objects.filter(status=False, solved=False, read=False).order_by('date')

        context = {
            'issue': issue,
        }
        return render(request, 'App_Admin/Issue/newissues.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def ContactusList(request):

    if request.user.is_staff:
        contactus = Contactus.objects.all().order_by('-pk')

        context = {
            'contactus': contactus
        }
        return render(request, 'App_Admin/Contactus/contactuslist.html', context)
    else:
        return render(request, 'notauthorised.html')


@login_required(login_url = '/login/')
def ContactusDetailsAdmin(request, pk):

    if request.user.is_staff:
        contactus = get_object_or_404(Contactus, pk=pk)

        if request.method == 'POST':
            form = ContactusDetails(request.POST or None, instance=contactus)
            if form.is_valid():
                form.save()
                return redirect('App_Admin:contactuslist')
        else:
            form = ContactusDetails(instance=contactus)

        context = {
            'contactus': contactus,
            'form':form
        }
        return render(request, 'App_Admin/Contactus/contactusdetails.html', context)
    else:
        return render(request, 'notauthorised.html')





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
