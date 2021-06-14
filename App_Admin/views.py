from django.shortcuts import render

# Create your views here.
def AdminHome(request):
    return render(request,'App_Admin/adminhome.html')

def AdminHome1(request):
    return render(request,'App_Admin/adminhome1.html')