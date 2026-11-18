from django.shortcuts import render

def home(request):
    skills=["Python","Django","HTML","CSS"]
    return render(request,'home.html',{"skills":skills})
