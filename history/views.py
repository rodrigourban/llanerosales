from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404
)
from django.views.decorators import require_http_methods


# Create your views here.
@require_http_methods(['GET', 'POST'])
def sell_item(request, pk):
    try:
        obj = get_object_or_404(Item, pk=pk)
    except Item.DoesNotExist:
        raise Http404("El articulo ingresado no existe")

    if request.method == 'GET':
        return render(
            request,
            'inventory/sell_item.html',
            {"item": obj, "form": sellForm()}
            )
    elif request.method == 'POST':
        form = sellForm(request.POST)
      