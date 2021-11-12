from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from adminPortfolio.models import UserInfo


class AccueilPortfolio(ListView):
    model = UserInfo
    template_name = "adminPortfolio/index.html"
    context_object_name = "infos"
