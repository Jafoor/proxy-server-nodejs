from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from App_Event.forms import CreateEventSubmit
from django.conf import settings
from App_Account.models import Organization
from App_Event.models import Event, Donation
from django.contrib import messages
from App_Admin.models import LandingPage, CommonField, Contactus
User = get_user_model()


# for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Home(request):

    landingpage = LandingPage.objects.filter().order_by('-id')[0]
    events = Event.objects.filter(active=True).order_by('clicked')
    context = {
        'landingpage': landingpage,
        'popularenvents': events
    }

    return render(request, 'App_Event/home.html', context)

def ContactUs(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        contactus = Contactus.objects.create(message=message, subject=subject)

        if request.user.is_authenticated:
            contactus.name = request.user.first_name
            contactus.email = request.user.email
            contactus.user = request.user

        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            contactus.name = name
            contactus.email = email
        contactus.save()
        messages.success(request,f"Your message has been sent Successfully")


    return render(request, 'App_Event/contactus.html')

def Eventdetails(request, slug):

    eventdetails = get_object_or_404(Event, slug=slug)
    if eventdetails.active == True and eventdetails.banned != True:

        if request.method == 'POST':
            amount = request.POST.get('amount')
            hide_identity = request.POST.get('hide_identity')
            print(hide_identity)
            if int(amount) <= 0:
                messages.warning(request, f"You have to give positive value")
                eventdonators = Donation.objects.filter(event=eventdetails, ordered=True)
                context = {
                    'eventdetails': eventdetails,
                    'eventdonators': eventdonators,
                }

                return render(request, 'App_Event/eventDetails.html', context)

            donations = Donation(event=eventdetails, amount=amount)
            if request.user.is_authenticated:
                name = request.user.first_name
                email = request.user.email
                donations.user = request.user
                donations.name = name
                donations.email=email
                if hide_identity == 'True':
                    donations.hide_identity = True
                donations.save()
            else:
                name = request.POST.get('name')
                email = request.POST.get('email')
                donations.name = name
                donations.email = email
                if hide_identity == 'True':
                    donations.hide_identity = True
                donations.save()
            store_id = 'shunn60d19f5306df0'
            API_key = 'shunn60d19f5306df0@ssl'
            mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

            status_url = request.build_absolute_uri(reverse("App_Event:complete", kwargs={'pk':donations.pk}))

            mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

            mypayment.set_product_integration(total_amount=Decimal(donations.amount), currency='BDT', product_category='Mixed', product_name="Donation", num_of_item=1, shipping_method='Digital', product_profile='None')

            mypayment.set_customer_info(name=donations.name, email=donations.email, address1="Not Needed", address2="Not Needed", city="Not Needed", postcode="Not Needed", country="Bangladesh", phone="01846825017")

            mypayment.set_shipping_info(shipping_to=donations.name, address="Not Needed", city="Not Needed", postcode="Not Needed", country="Bangladesh")

            response_data = mypayment.init_payment()
            return redirect(response_data['GatewayPageURL'])

        eventdonators = Donation.objects.filter(event=eventdetails, ordered=True)
        context = {
            'eventdetails': eventdetails,
            'eventdonators': eventdonators,
        }

        return render(request, 'App_Event/eventDetails.html', context)
    elif eventdetails.banned == True:
        return render(request, 'bannedevent.html')
    else:
        return render(request, 'inactiveevent.html')


@csrf_exempt
def complete(request, pk):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,f"Your Donation Completed Successfully! Page will be redirected!")
            return HttpResponseRedirect(reverse("App_Event:purchase", kwargs={'val_id':val_id, 'tran_id':tran_id, 'pk':pk}))
        elif status == 'FAILED':
            messages.warning(request, f"Your Donation Failed! Please Try Again! Page will be redirected!")

    return render(request, "Payment/complete.html", context={})


def purchase(request, val_id, tran_id, pk):
    order = Donation.objects.get(pk=pk, ordered=False)
    eventid = order.event
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.save()
    event = get_object_or_404(Event, pk=eventid.pk)
    event.collected += int(order.amount)
    event.save()
    return HttpResponseRedirect(reverse("App_Event:eventdetails", kwargs={'slug':event.slug}))

@login_required(login_url = '/login/')
def OrgApplyevent(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        if request.method == 'POST':
            form = CreateEventSubmit(request.POST or None, request.FILES or None)
            if form.is_valid():
                event = form.save(commit=False)
                event.user = user
                event.active = True
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
    else:
        return render(request, 'notauthorised.html')

@login_required(login_url = '/login/')
def OrgEventList(request, slug):

    user = get_object_or_404(User, slug=slug)
    if request.user == user:
        org = get_object_or_404(Organization, org=user)
        events = Event.objects.filter(user = org.org)
        print(events)
        context = {
            'user': user,
            'org': org,
            'events': events,
        }


        return render(request, 'App_Organization/orgeventlist.html', context)
    else:
        return render(request, 'notauthorised.html')
