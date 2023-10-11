from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def mypage(request):
    return render(request, 'home/mypage.html')
# Create your views here.
