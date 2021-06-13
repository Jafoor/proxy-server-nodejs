from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from App_Account.models import Organization
# Create your views here.
User = get_user_model()
def OrgDashboard(request, slug):

    user = get_object_or_404(User, slug=slug)
    org = get_object_or_404(Organization, org=user)
    context = {
        'user': user,
        'org': org
    }
    return render(request, 'App_Organization/OrganizationDashboard.html', context )
