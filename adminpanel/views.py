from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
# create custon login template
# add users, roles, employee, manager, admin.
# add created_by/edited_by fields to models
# admin panel with user managment.
# -admin panel get ganancias, with charts

@require_http_methods(['GET'])
def admin_panel(request):
    return render(
        request,
        'admin/index.html'
    )

@require_http_methods(['GET', 'POST'])
def create_user(request):
    if request.method == 'GET':
        return render(
            request,
            'admin/create_user.html',
            {'form': UserCreationForm}
        )
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(
                request,
                "Cuenta creada exitosamente"
            )
        else:
            messages.error(
                request,
                "Por favor ingresa informacion valida"
            )
            return redirect('admin-panel:create-user')
        return redirect('admin-panel:index')


@require_http_methods(['GET', 'DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        return render(
            request,
            'admin-panel:delete-user',
            {'object': user}
        )
    elif request.method == 'DELETE':
        user.is_active = False
        user.save()
        messages.success(
            request,
            "Se borro el usuario correctamente"
        )
        return render(
            request,
            'admin:index'
        )


@require_http_methods(['POST'])
def get_earnings_charts(request):
    pass
