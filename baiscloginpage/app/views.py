from django.shortcuts import render

# Create your views
def login(request):
    return render(request,'login.html')
