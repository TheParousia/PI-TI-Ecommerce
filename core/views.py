import os
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage()

from core import models

def front_end(request):
    template = loader.get_template("tela_produto.html")
    return HttpResponse(template.render())