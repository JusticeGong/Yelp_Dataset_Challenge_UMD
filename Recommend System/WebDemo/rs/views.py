from django.shortcuts import render
from django.http import HttpResponse, Http404
from rs.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
# from rs.forms import *
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.http import HttpResponse

from .models import rec


def index(request):
    # all_rating = rec.objects.all()[:5]
    # a = ''
    # for a in all_rating:
    #     a += '<h1>' + str(rec.uID) + '</h1>'
    return HttpResponse("<h1>asd</h1>")


# def detail(request, uID):
#     all_rating = rec.objects.all()[:5]
#     a = ''
#     for a in all_rating:
#         a += '<h1>' + str(rec.uID) + '</h1>'
#     return HttpResponse(a)

