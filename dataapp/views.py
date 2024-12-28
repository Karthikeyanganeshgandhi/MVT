from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader/
from .models import user

def login(request):
    logindetails = user.objects.all()
    return render(request,'userpage.html',{'logindetails': logindetails})
