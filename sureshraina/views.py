from django.shortcuts import render

# Create your views here.
def suresh(request):
    d={'name':"Gangadhara"}
    return render(request, 'raina.html',context=d)