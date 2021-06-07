from django.shortcuts import render
import datetime
import json
import os


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Каталог', 'products': json.load(
        open(os.path.join(os.path.dirname(__file__), 'fixtures/goods.json'), encoding='utf-8'))}
    return render(request, 'products/products.html', context)


def cap_and_date_now(request):
    return render(request, 'products/cap_and_date_now.html')
