from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from shortener_api import models
from django.shortcuts import render



def redirect_real_url(request, hash_url):
    url = get_object_or_404(models.Urls, hash_url=hash_url)
    url.clicked()
    return redirect(url.url)


def render_home_page(request):
    return render(request, 'shortener_page/index.html')
