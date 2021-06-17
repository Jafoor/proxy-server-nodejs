from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'App_Admin/master.html')

def AdminHome(request):
    return render(request,'App_Admin/adminhome.html')

def organizations(request):
    return render (request,'App_Admin/organizations.html')

def verifiedusers(request):
    return render (request,'App_Admin/verifiedusers.html')

def generalusers(request):
    return render (request,'App_Admin/generalusers.html')

def eventsbyusers(request):
    return render (request,'App_Admin/eventsbyusers.html')

def eventsbyorganizations(request):
    return render (request,'App_Admin/eventsbyorganiztions.html')