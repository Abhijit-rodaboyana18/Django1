from django.shortcuts import render

# Create your views here.
from .models import emp
def admin_home(request):
    a = emp
    return render(request,'admin_home.html',{'con':a})
