from django.shortcuts import render, redirect


# Create your views here.

def myHome(request):

    return render(request,"index.html")