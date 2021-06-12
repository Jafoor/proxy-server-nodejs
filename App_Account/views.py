from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import UserRegistrationForm, UserLoginForm, OrganizationForm
from .models import EmailConfirmation, Organization

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

            # user = EmailConfirmation.objects.get(user=instance)
            # site = get_current_site(request)
            # email = instance.email
            # first_name = instance.first_name
            # last_name = instance.last_name
            # email_body = render_to_string(
            #     'App_Account/varify_email.html',
            #     {
            #         'first_name': first_name,
            #         'last_name': last_name,
            #         'email': email,
            #         'domain': site.domain,
            #         'activation_key':  user.activation_key
            #     }
            # )
            # send_mail(
            #     subject = 'Email Confirmation',
            #     message = email_body,
            #     from_email = 'shunnoek.bd@gmail.com',
            #     recipient_list = [email],
            #     fail_silently = True
            # )
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
                return redirect('home')
            else:
                return render(request, 'App_Account/registration_varification.html')
        return render(request, 'App_Account/login.html', {'form': form})
    return render(request, 'App_Account/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def email_confirm(request, activation_key):
    user = get_object_or_404(EmailConfirmation, activation_key= activation_key)
    if user is not None:
        user.email_confirmed = True
        user.save()

        instance = User.objects.get(email=user)
        instance.is_active = True
        instance.save()

        return render(request, 'App_Account/registration_complete.html')
