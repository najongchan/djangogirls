from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
import requests, json

from .models import Tenor
from .form import Tenorform


def tenor_list(request):
    form = Tenorform(request.GET)
    tenor = Tenor()
    search_term = "excited"
    if form.is_valid():
        search_term = form.data['search_term']
    res = tenor.searchGifs(search_term)
    return render(request, 'tenor/tenor_list.html',
                  {'tenor': tenor, 'res': res, 'results': res['results'], 'form': form, 'search_term': search_term})


@require_POST
def gif_send(request):
    print(request)
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        image_url = request.POST.get('image_url')
        print(search_term)
        print(image_url)
        tenor = Tenor()
        res = tenor.sendDoorayGifMessage(search_term, image_url)
        print(res)

    return res
