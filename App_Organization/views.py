from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization, VerifyOrgBankDetails
from App_Organization.forms import OrgDocumentsSubmit
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

def Organizationformation(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    context = {
        'user': user,
        'org': org
    }
    return render(request, 'App_Organization/OrganizationInformation.html', context )

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
        bankinfo.is_verified = True
        bankinfo.save()
    bankinfo = get_object_or_404(VerifyOrgBankDetails, user=user)
    context = {
        'user': user,
        'org': org,
        'bankinfo': bankinfo
    }
    # if request.user == user:
    return render(request, 'App_Organization/updatebankinformation.html', context )



def UpdateOrganizationInformation(request, slug):

    user = get_object_or_404(User, slug=slug)
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
        print(org_about)
        print(thana)
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

    # if request.user == user:
    return render(request, 'App_Organization/updateorganizationinformation.html', context )


def OrganizationDocuments(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    context = {
        'user': user,
        'org': org
    }
    return render(request, 'App_Organization/OrganizationDocuments.html', context )

def UpdateOrganizationDocuments(request, slug):
    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    if request.method == 'POST':
        form = OrgDocumentsSubmit(request.POST or None, request.FILES or None,instance=org)
        if form.is_valid():
            form.save()
            return redirect('App_Organization:OrganizationDashboard', slug)
    else:
        form = OrgDocumentsSubmit(instance=org)
    context = {
        'user': user,
        'org': org,
        'form': form,
    }

    return render(request, 'App_Organization/updateorganizationdocuments.html', context)
