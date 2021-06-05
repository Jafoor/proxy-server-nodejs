from django.shortcuts import render

# Create your views here.

def Home(request):

    return render(request, 'App_Event/home.html')

def Contactus(request):

    return render(request, 'App_Event/contactus.html')

def Eventdetails(request):

    return render(request, 'App_Event/eventDetails.html')

def Applyevent(request):

    return render(request, 'App_Event/applyevent.html')
