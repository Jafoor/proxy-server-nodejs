from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization, VerifyOrgBankDetails
# Create your views here.
User = get_user_model()

def OrgDashboard(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    context = {
        'user': user,
        'org': org
    }
    return render(request, 'App_Organization/home.html', context )

def BankInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    context = {
        'user': user,
        'org': org
    }
    return render(request, 'App_Organization/bankinformation.html', context )

def UpdateBankInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    bankinfo = get_object_or_404(VerifyOrgBankDetails, user=user)
    if request.method == 'POST':
        bank_name = request.POST.get("bank_name")
        bank_branch = request.POST.get("bank_branch")
        account_name = request.POST.get("account_name")
        account_number = request.POST.get("account_number")
        bankinfo.bank_name = bank_name
        bankinfo.bank_branch = bank_branch
        bankinfo.account_name = account_name
        bankinfo.account_number = account_number
        bankinfo.save()
    context = {
        'user': user,
        'org': org,
        'bankinfo': bankinfo
    }
    # if request.user == user:
    return render(request, 'App_Organization/updatebankinformation.html', context )
