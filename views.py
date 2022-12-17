# I have Created this file - Adarsh
from django.http import HttpResponse
from django.shortcuts import render


# 1. Personal Navigator

# def index(request):
#     return HttpResponse('''<h1>Hello Adarsh Vajpayee!! this is </h1>
#                         <a href="https://docs.djangoproject.com/en/4.1/"</a>Django''')
#
# def about(request):
#     return HttpResponse("About Adarsh Vajpayee")

# 2. Laying the pipeline.

# def index(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("Removepunc")
#
# def newlineremove(request):
#     return HttpResponse("New line remover")
#
# def capfirst(request):
#     return HttpResponse("captialize first")
#
# def spaceremove(request):
#     return HttpResponse("Space remover")
#
# def charcount(request):
#     return HttpResponse("Character counter")

# 3.Templates in django by importing render.

# def index(request):
#     params = {'name':'adarsh','place':'raichur'}
#     return render(request, 'index.html',params)
#     # return HttpResponse("Home")
#
#
# def removepunc(request):
#     return HttpResponse("Removepunc")
#
#
# def newlineremove(request):
#     return HttpResponse("New line remover")
#
#
# def capfirst(request):
#     return HttpResponse("captialize first")
#
#
# def spaceremove(request):
#     return HttpResponse("Space remover")
#
#
# def charcount(request):
#     return HttpResponse("Character counter")

# 4.Creating homepage of textutils Website.

# def index(request):
#     return render(request, 'index.html')
#     # return HttpResponse("Home")
#
#
# def removepunc(request):
#     # Get the text.
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze The text.
#     return HttpResponse("Removepunc")
#
#
# def newlineremove(request):
#     return HttpResponse("New line remover")
#
#
# def capfirst(request):
#     return HttpResponse("captialize first")
#
#
# def spaceremove(request):
#     return HttpResponse("Space remover")
#
#
# def charcount(request):
#     return HttpResponse("Character counter")
#

# 5. Coding the backend.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyse(request):
    # Get text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)
    if removepunc == "on":
        # Analyse Text
        # return HttpResponse("remove punc")
        punctuations = '''!()-[]{};:'"\,<>./?@$%^&*_~'''
        analysed = ''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed+char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analysed}
        # return render(request, 'analyse.html',params)
        djtext=analysed
    if(fullcaps == 'on'):
        analysed = ''
        for char in djtext:
            analysed = analysed+char.upper()
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', params)
    if(newlineremover == 'on'):
        analysed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed = analysed + char
        print("pre", analysed)
        params = {'purpose': 'New Line Remover', 'analyzed_text': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', params)
    if(spaceremover == 'on'):
        analysed = ''
        for char in djtext:
            if char != ' ':
                analysed = analysed + char
        params = {'purpose': 'space remover', 'analyzed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)
    if(extraspaceremover == 'on'):
        analysed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analysed = analysed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analysed}
        djtext = analysed
    if (removepunc != 'on' and newlineremover != 'on' and spaceremover!='on' and fullcaps!='on' and extraspaceremover!='on'):
        return HttpResponse("Please Select Any Operation.")
        # return render(request, 'analyse.html', params)
    return render(request, 'analyse.html', params)


# Personal Navigator Solution.
def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
    <a href="https://www.facebook.com/">FaceBook</a><br>
    <a href="https://www.filpkart.com/">FilpKart</a><br>
    <a href="https://www.hindustantimes.com/">Hindustan Times</a><br>
    <a href="https://www.github.com/">Github</a><br>
    <a href="https://www.instagram.com/">Instagram</a><br>
    '''
    return  HttpResponse(s)
