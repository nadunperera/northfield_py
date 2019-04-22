from django.shortcuts import render, get_object_or_404
from .models import Asset


# Create your views here.

def asset_list_view(request):
    qs = Asset.objects.all()
    page_title = 'All Assets'
    template_name = 'asset_list.html'
    context = {'object_list': qs, 'page_title': page_title}
    return render(request, template_name, context)


def asset_create_view(request):
    template_name = 'asset_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def asset_detail_page(request, asset_id):
    # obj = Asset.objects.get(id=asset_id)
    obj = get_object_or_404(Asset, id=asset_id)
    template_name = 'asset_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def asset_update_view(request, asset_id):
    obj = get_object_or_404(Asset, id=asset_id)
    template_name = 'asset_detail.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def asset_delete_view(request, asset_id):
    obj = get_object_or_404(Asset, id=asset_id)
    template_name = 'asset_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)
