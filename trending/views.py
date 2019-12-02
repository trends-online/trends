from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import models

def homepage(request):
    general = models.trends.objects.filter(type='general').order_by('-id')
    sports = models.trends.objects.filter(type='sports').order_by('-id')
    technology = models.trends.objects.filter(type='technology').order_by('-id')
    social = models.social.objects.all().order_by('-id')
    search_input = request.POST.get('search', False);
    if search_input == None:
        search = models.trends.objects.all()
    else:
        search = models.trends.objects.filter(keywords__icontains=search_input)
    return render(request, 'homepage.html', {'general':general, 'sports':sports, 'technology':technology, 'search':search, 'social':social})

def article(request, id):
    article = models.trends.objects.filter(id=id)
    social = models.social.objects.all().order_by('-id')
    search_input = request.POST.get('search', False);
    if search_input == None:
        search = models.trends.objects.all()
    else:
        search = models.trends.objects.filter(keywords__icontains=search_input)
    return render(request, 'article.html', {'article':article, 'social':social, 'search':search})