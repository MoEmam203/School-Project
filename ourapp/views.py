from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'ourapp/home.html')


def login(request):
    return render(request,'ourapp/login/index.html')
