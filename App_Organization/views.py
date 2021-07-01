from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization, VerifyOrgBankDetails
from django.contrib.auth.decorators import login_required
from App_Organization.forms import OrgDocumentsSubmit, OrgWithdraw, CreateIssue
from App_Event.models import Event, Donation, Withdraw
from App_Admin.models import SupportedBanks, Issue
from datetime import datetime
from decimal import Decimal
from django.contrib import messages


# Create your views here.
User = get_user_model()

@login_required(login_url = '/login/')
def OrgDashboard(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        orgbank = get_object_or_404(VerifyOrgBankDetails, user=user)
        event = Event.objects.filter(user=user).count()
        current_event = Event.objects.filter(user=user,
                                             endtime__gt = datetime.now()
                                              ).count()
        context = {
            'user': user,
            'org': org,
            'orgbank': orgbank,
            'event' : event,
            'currentevent': current_event
        }
        return render(request, 'App_Organization/home.html', context )
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def BankInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        banks = SupportedBanks.objects.filter(active=True).order_by('name')
        bankinfo = get_object_or_404(VerifyOrgBankDetails, user=user)
        print(bankinfo)
        context = {
            'user': user,
            'org': org,
            'bankinfo': bankinfo,
            'banks': banks
        }
        return render(request, 'App_Organization/bankinformation.html', context )
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def Organizationformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        context = {
            'user': user,
            'org': org
        }
        return render(request, 'App_Organization/OrganizationInformation.html', context )
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UpdateBankInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        bankinfo = get_object_or_404(VerifyOrgBankDetails, user=user)
        banks = SupportedBanks.objects.filter(active=True).order_by('name')
        if request.method == 'POST':
            bank_name = request.POST.get("bank_name")
            bank_branch = request.POST.get("bank_branch")
            account_name = request.POST.get("account_name")
            account_number = request.POST.get("account_number")
            bankinfo.bank_name = bank_name
            bankinfo.bank_branch = bank_branch
            bankinfo.account_name = account_name
            bankinfo.account_number = account_number
            bankinfo.is_verified = True
            bankinfo.save()
            return redirect('App_Organization:OrganizationDashboard', slug)
        context = {
            'user': user,
            'org': org,
            'bankinfo': bankinfo,
            'banks': banks
        }
        # if request.user == user:
        return render(request, 'App_Organization/updatebankinformation.html', context )
    else:
        return render(request, 'notauthorised.html')


@login_required(login_url = '/login/')
def UpdateOrganizationInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        context = {
            'user': user,
            'org': org,
        }

        if request.method == 'POST':
            contact_number = request.POST.get('contact_number')
            org_about = request.POST.get('org_about')
            org_type = request.POST.get('org_type')
            org_active_member = request.POST.get('org_active_member')
            division = request.POST.get('division')
            zilla = request.POST['zilla']
            thana = request.POST.get('thana')
            address = request.POST.get('address')
            socila_link1 = request.POST.get('socila_link1')
            socila_link2 = request.POST.get('socila_link2')
            org.contact_number = contact_number
            org.org_about = org_about
            org.org_type= org_type
            org.org_active_member = org_active_member
            org.division = division
            org.zilla = zilla
            org.thana = thana
            org.address = address
            org.socila_link1 = socila_link1
            org.socila_link2 = socila_link2
            org.given_org_details = True
            org.save()
            return redirect('App_Organization:OrganizationDashboard', slug)

        return render(request, 'App_Organization/updateorganizationinformation.html', context )
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def OrganizationDocuments(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        context = {
            'user': user,
            'org': org
        }
        return render(request, 'App_Organization/OrganizationDocuments.html', context )
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def UpdateOrganizationDocuments(request, slug):
    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        if request.method == 'POST':
            form = OrgDocumentsSubmit(request.POST or None, request.FILES or None,instance=org)
            if form.is_valid():
                f = form.save(commit=False)
                f.given_org_documents = True
                f.save()
                return redirect('App_Organization:OrganizationDashboard', slug)
        else:
            form = OrgDocumentsSubmit(instance=org)
        context = {
            'user': user,
            'org': org,
            'form': form,
        }

        return render(request, 'App_Organization/updateorganizationdocuments.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def WithdrawAmount(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        orgbank = get_object_or_404(VerifyOrgBankDetails, user=user)
        if request.method == 'POST':
            form = OrgWithdraw(request.POST or None)
            if form.is_valid():
                amount = form.cleaned_data['amount']
                amount = Decimal(amount)
                if amount > Decimal(orgbank.current_balance) or amount <= 0.0:
                    messages.error(request, "You don't have enough balance to withdraw.")
                    return redirect('App_Organization:withdrawamount', slug)
                form.save(commit=False)
                form.user=user
                form.save()
                return redirect('App_Organization:withdrawlist', slug)

        form = OrgWithdraw()

        context = {
            'user': user,
            'org': org,
            'form': form,
            'orgbank': orgbank
        }

        return render(request, 'App_Organization/withdrawamount.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def WithdrawList(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)

        withdraw = Withdraw.objects.filter(user=user)

        context = {
            'user': user,
            'org': org,
            'withdraw': withdraw
        }

        return render(request, 'App_Organization/withdrawlist.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def CreateIssueOrg(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)

        if request.method == 'POST':
            form = CreateIssue(request.POST or None)
            if form.is_valid():
                f = form.save(commit=False)
                f.user=user
                f.save()
                return redirect('App_Organization:issuelist', slug)
        else:
         form = CreateIssue()

        context = {
            'user': user,
            'org': org,
            'form': form
        }

        return render(request, 'App_Organization/createissue.html', context)
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def issuelist(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)

        issue = Issue.objects.filter(user=user)

        context = {
            'user': user,
            'org': org,
            'issue': issue
        }

        return render(request, 'App_Organization/issuelist.html', context)
    else:
        return render(request, 'notauthorised.html')
