from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def videos(request):
    return render(request,"videos.html")

@login_required
def python(request):
    return render(request,"python.html")

@login_required
def cpp(request):
    return render(request,"cpp.html")

@login_required
def django(request):
    return render(request,"django.html")

@login_required
def javascript(request):
    return render(request,"javascript.html")


@login_required
def java(request):
    return render(request,"java.html")

@login_required
def nodejs(request):
     return render(request,"nodejs.html")

@login_required
def reactjs(request):
     return render(request,"reactjs.html")

@login_required
def ruby(request):
     return render(request,"ruby.html")