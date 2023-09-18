  

from django.http import HttpResponse
from django.shortcuts import render
# def HomePage(request):
    # return render(request,"index.html")
    
def Index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
    # return HttpResponse("welcome to django")
def course(request):
    return HttpResponse("welcome to django2")
def course(request):
    return HttpResponse("<b>welcome to django3</b>")
def courseDetails(request,courseid):
    return HttpResponse(courseid)