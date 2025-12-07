from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Item


# Create your views here.
def index(request):
    context = {
        "msg": "Hola Somos VShop by Victoria Romero"
    }

    return render(request, "core/index.html", context)

def home(request):
    items = Item.objects.filter(is_sold=False)[0:20]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {
        'item': item,
        'related_items': related_items
    }

    return render(request, 'core/item.html', context)
