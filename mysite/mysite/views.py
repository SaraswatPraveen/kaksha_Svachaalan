from django.shortcuts import render
from subprocess import run
import sys
def button(request):
    return render(request,"home1.html")
def output(request):
    data = 2 * 2
    return render(request,'home1.html')
def external(request):
    out = run([sys.executable,'\\Users\\shiva\\Desktop\\NewPro\\New folder\\test.py'],shell=False)
    return render(request,"home1.html")