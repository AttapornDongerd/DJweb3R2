from django.shortcuts import render,HttpResponse

# Create your views here.
def helloword(request):
    return HttpResponse("<H1>Hello word, this is my First Django Web </H1>"
                        "<H2>I Love Python and Django,It's My Life</H2>")
def firstpage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def Hnypage(request):
    return render(request, 'Hnypage.html')

def home(request):
    return render(request, 'home.html')
