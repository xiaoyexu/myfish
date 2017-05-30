from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.utils import timezone
from models import *

def THR(request, template, context):
    """Return HttpResponse object with template and context"""
    template = loader.get_template(template)
    ctx = RequestContext(request, context)
    return HttpResponse(template.render(ctx))


# Create your views here.
def index(request):
    fps = FishPhoto.objects.all().order_by('-createdAt')
    fp = None
    lastTime = None

    if fps:
        fp = fps[0]
        lastTime = timezone.localtime(fp.createdAt)
    return THR(request, 'index.html', {'fp':fp, 'lastTime': lastTime})

class PhotoForm(forms.Form):
    file = forms.ImageField()

"""
<form action="upload" method="POST" enctype="multipart/form-data">
    <input type="file" name="file"/>
    <input type="submit" name="submit" text="upload"/>
</form>
"""

@csrf_exempt
def upload(request):
    # pf = PhotoForm(request.POST, request.FILES)
    # if not pf.is_valid():
    #     return THR(request, 'index.html', {})
    # upfile = pf.cleaned_data['file']
    upfile = request.FILES.get('fishphotofile', None)
    fp = None
    lastTime = None
    if upfile:
        fp = FishPhoto()
        fp.photo = upfile
        fp.save()
    return THR(request, 'index.html', {'fp': fp})

def forbidden(request):
    return THR(request, '404.html',{})