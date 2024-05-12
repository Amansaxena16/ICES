from django.shortcuts import render

def index(request):
    title = {'title' : 'ICES School'}
    return render(request,'index.html',title)    

def test(request):
    return render(request,'test.html')
