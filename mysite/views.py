#I have created this file - Muhammad Basit Hussain
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click me</a>''')
def analyzer(request):
    djtext = request.GET.get('text','default')
    djcheck = request.GET.get('check','default')
    print(djtext[0])
    param = {'purpose':'Remove Punctuation','analyzed_text':djtext}
    return render(request,'about.html',param)