from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(request):
    return render(request, 'home.html')

def Count(request):
    Words = request.GET['fulltext']
    allwords = Words.split()
    wordDictionary = {}
    for word in allwords:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    wordSorted = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'wordDictionary' : wordSorted, 'words': len(allwords), 'fulltext': Words})

def About(request):
    return render(request, 'about.html')