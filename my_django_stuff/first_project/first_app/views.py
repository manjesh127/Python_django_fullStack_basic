from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("hello world")
    my_dic = {'insert_me':"now i am coming from first/index.html"}
    return render(request,'firstapp/index.html',context=my_dic)