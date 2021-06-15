from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'App_Admin/master.html')

def AdminHome(request):
    return render(request,'App_Admin/adminhome.html')