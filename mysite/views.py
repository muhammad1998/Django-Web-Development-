#I have created this file - Muhammad Basit Hussain
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click me</a>''')
def analyzer(request):
    djtext = request.GET.get('text','default')
    djcheck = request.GET.get('check','off')
    if djcheck == "on":
        analyzer_text = ""
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in Punctuations:
                analyzer_text = analyzer_text+char
    

        param = {'purpose':'Remove Punctuation','analyzed_text':analyzer_text}
    else:
        param = {'purpose':'Remove Punctuation','analyzed_text':djtext}
        
    return render(request,'about.html',param)