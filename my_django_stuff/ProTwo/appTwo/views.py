from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>my second project</em>")

def help(request):
    helpdict={'help_insert':"help page"}
    return render(request,'second/index.html',context = helpdict)    