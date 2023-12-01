from django.shortcuts import render,redirect

def myhome(request):

    return render(request,"index.html")