from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def login(request):
    return render(request, 'index/login.html')

def regist(request):
    return render(request, 'index/regist.html')