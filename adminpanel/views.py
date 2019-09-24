from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

# create custon login template
# add users, roles, employee, manager, admin.
# add created_by/edited_by fields to models
# admin panel with user managment.
# -admin panel get ganancias, with charts

@require_http_methods(['GET'])
def admin_panel(request):
    pass

@require_http_methods(['GET', 'POST'])
def create_user(request):
    pass

@require_http_methods(['DELETE'])
def delete_user(request):
    pass

@require_http_methods(['POST'])
def get_earnings_charts(request):
    pass
