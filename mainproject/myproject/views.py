from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponseBadRequest, HttpResponse
import pandas as pd
import numpy as np
import requests
from django.shortcuts import render
import subprocess
import multiprocessing
import time  

#Create your views here  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def test(request):
        subprocess.call(["python", "myproject\drowsinessdetection.py"])


def index(request):
    return render(request,"index.html")

def output(request):
    print('EDA')
    

    p = multiprocessing.Process(target=test, name="test", args=(10,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(10)

    if p.is_alive():
        print("foo is running... let's kill it...")
        p.terminate()
        p.join()


    from django.http import HttpResponse
    return HttpResponse(status=204)



def output2(request):
    print('EDA Hey hey')
    from django.http import HttpResponse
    return HttpResponse(status=204)

  





