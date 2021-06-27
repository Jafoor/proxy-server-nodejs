from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
from App_Account.forms import UserRegistrationForm, UserLoginForm, OrganizationForm, UserInfo
from App_Account.models import EmailConfirmation, Organization, Profile, VerifyPersonBankDetails
from App_Event.models import Event, Donation, Report
from App_Account.generaluserform import UserBankProfile, Withdraw
from App_Event.forms import CreateEventSubmit
from decimal import Decimal

User = get_user_model()

# Create your views here.

def register_organization(request):

    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            instance = form.save(commit=False)
            instance.is_active = False
            instance.is_org = True
            instance.save()


            contact_number = request.POST.get('office_number')
            org_about = request.POST.get('obout_org')
            new_org = Organization.objects.get(org=instance)
            instance.refresh_from_db()
            new_org.contact_number = contact_number
            new_org.org_about = org_about
            new_org.org_name = instance.first_name
            new_org.save()

            user = EmailConfirmation.objects.get(user=instance)
            site = get_current_site(request)
            email = instance.email
            first_name = instance.first_name
            email_body = render_to_string(
                'App_Account/varify_email_org.html',
                {
                    'first_name': first_name,
                    'email': email,
                    'domain': site.domain,
                    'activation_key':  user.activation_key
                }
            )
            send_mail(
                subject = 'Email Confirmation',
                message = email_body,
                from_email = 'shunnoek.bd@gmail.com',
                recipient_list = [email],
                fail_silently = True
            )
            return render(request, 'App_Account/registration_varification.html')
        return render(request, 'App_Account/registration_organization.html', {'form': form})
    return render(request,'App_Account/registration_organization.html',{'form': form})

def register(request):

    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            instance = form.save(commit=False)
            instance.is_active = False
            instance.save()


            user = EmailConfirmation.objects.get(user=instance)
            site = get_current_site(request)
            email = instance.email
            first_name = instance.first_name
            last_name = instance.last_name
            email_body = render_to_string(
                'App_Account/varify_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'domain': site.domain,
                    'activation_key':  user.activation_key
                }
            )
            send_mail(
                subject = 'Email Confirmation',
                message = email_body,
                from_email = 'shunnoek.bd@gmail.com',
                recipient_list = [email],
                fail_silently = True
            )
            return render(request, 'App_Account/registration_varification.html')
        return render(request, 'App_Account/registration.html', {'form': form})
    return render(request, 'App_Account/registration.html', {'form': form})


def login_view(request):
    _next = request.GET.get('next')
    print(_next)
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            if request.user.is_active:
                if _next:
                    return redirect(_next)
                return redirect('App_Event:home')
            else:
                return render(request, 'App_Account/registration_varification.html')
        return render(request, 'App_Account/login.html', {'form': form})
    return render(request, 'App_Account/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('App_Account:login')

def email_confirm(request, activation_key):
    user = get_object_or_404(EmailConfirmation, activation_key= activation_key)
    if user is not None:
        user.email_confirmed = True
        user.save()

        instance = User.objects.get(email=user)
        instance.is_active = True
        instance.save()

        return render(request, 'App_Account/registration_complete.html')

def generaluserdashboard(request, slug):

    user = get_object_or_404(User, slug=slug)
    donations = Donation.objects.filter(user=user)
    profile = get_object_or_404(Profile, user=user)
    bankinfo = get_object_or_404(VerifyPersonBankDetails, user=user)
    totalamount = 0
    for i in donations:
        totalamount += i.amount

    context = {
        'user' : user,
        'profile': profile,
        'donations': donations,
        'totalamount': totalamount,
        'bankinfo': bankinfo
    }

    return render (request, 'generaluser/dashboard.html', context)


def updatepersonalinfo(request, slug):

    usr = get_object_or_404(User, slug=slug)
    profile = get_object_or_404(Profile, user=usr)

    if request.method == 'POST':
        form = UserInfo(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            division = request.POST.get('division')
            zilla = request.POST['zilla']
            thana = request.POST.get('thana')
            profile.division = division
            profile.zilla = zilla
            profile.thana = thana
            profile.save()
            return redirect('App_Account:profile', slug)
    else:
        form = UserInfo(instance=profile)

    context = {
        'form': form,
    }

    return render (request, 'generaluser/updateinfo.html', context)

def updatepersonalbankinfo(request, slug):

    usr = get_object_or_404(User, slug=slug)
    bankinfo = get_object_or_404(VerifyPersonBankDetails, user=usr)

    if request.method == 'POST':
        form = UserBankProfile(request.POST or None, request.FILES or None, instance=bankinfo)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            bankinfo.filled = True
            bankinfo.save()
            return redirect('App_Account:profile', slug)
    else:
        form = UserBankProfile(instance=bankinfo)

    context = {
        'form': form,
    }

    return render (request, 'generaluser/updatebankinfo.html', context)


def PersonApplyevent(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.method == 'POST':
        form = CreateEventSubmit(request.POST or None, request.FILES or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = user
            event.save()
            return redirect('App_Account:profile', slug)
    else:
        form = CreateEventSubmit()
    context = {
        'form': form,
    }


    return render(request, 'generaluser/createevent.html', context)




# Person Organization

def personorgdashboard(request, slug):

    user = get_object_or_404(User, slug=slug)
    events = Event.objects.filter(user=user)
    profile = get_object_or_404(Profile, user=user)
    bankinfo = get_object_or_404(VerifyPersonBankDetails, user=user)

    context = {
        'user' : user,
        'profile': profile,
        'events': events,
        'bankinfo': bankinfo
    }

    return render (request, 'personorg/dashboardpersonorg.html', context)

def eventsummery(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = get_object_or_404(User, slug=event.user.slug)
    donations = Donation.objects.filter(event=event, ordered=True)

    context = {
        'event': event,
        'donations': donations,
        'user': user
    }

    return render(request, 'personorg/eventsummery.html', context)

def withdrawbalance(request, slug):

    user = get_object_or_404(User, slug=slug)
    personbank = get_object_or_404(VerifyPersonBankDetails, user=user)
    if request.method == 'POST':
        form = Withdraw(request.POST or None)
        if form.is_valid():

            amount = form.cleaned_data['amount']
            amount = Decimal(amount)
            current = Decimal(personbank.current_balance)
            if current < amount:
                messages.error(request, "You don't have enough balance to withdraw.")
                return redirect('App_Account:withdrawbalance', slug)

            form.save(commit=False)
            form.user = user
            form.save()
            return redirect('App_Account:verifiesperson', slug=user.slug )
    else:
        form = Withdraw()

    context = {
        'form': form,
        'personbank': personbank,
    }

    return render(request, 'personorg/withdraw.html', context)
