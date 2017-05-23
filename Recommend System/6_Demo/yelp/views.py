from django.shortcuts import render
from yelp.models import *
# Create your views here.
from django.http import HttpResponse, Http404
from watershed.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from watershed.forms import *
from django.http import Http404
from yelp.forms import *


# #Generate GeoRSS
# def GeoRSS

# def index(request):
#     template_name = 'yelp/index.html'
#     return render(request, template_name)



def detail(request):
    template_name = 'yelp/detail.html'
    return render(request, template_name)

def index(request):
    all_uID = rec.objects.values('uID').distinct()
    form = NameForm(request.POST or None)
    context = {
        'all_uID': all_uID,
    }
    return render(request, 'yelp/index.html', context)

def googlemap(request):
    template_name = 'yelp/map.html'
    return render(request, template_name)

#AIzaSyAjYOJX3zs_QtedWHTGSaSGU01LjiPAMkc

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

