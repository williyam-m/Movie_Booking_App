from django.shortcuts import render, redirect, get_object_or_404
from .models import Screen
from django.contrib.auth.decorators import login_required
from user.views import role_required
from django.views.decorators.http import require_http_methods
import string
from django.contrib import messages
from theatre.models import *


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
def register(request):
    screen_list = Screen.objects.all()
    return render(request, 'screen_dashboard.html', {'screen_list': screen_list})


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
def screen_dashboard(request):
    screen_list = Screen.objects.all()
    return render(request, 'screen_dashboard.html', {'screen_list': screen_list})

@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@require_http_methods(["GET", "POST"])
def create_screen(request):
    theatres = Theatre.objects.all()
    if request.method == "POST":
        theatre_id = request.POST.get('theatre_id')
        name = request.POST.get('name')
        ticket_price = request.POST.get('ticket_price')
        rows = request.POST.get('rows')
        columns = request.POST.get('columns')

        if not 1 <= int(rows) <= 26:
            messages.info(request, 'Rows must be between 1 to 26')
            return render(request, 'create_screen.html', {'theatres': theatres})

        theatre = Theatre.objects.get(id = theatre_id)
        Screen.objects.create(
            theatre=theatre,
            name=name,
            ticket_price=ticket_price,
            rows=rows,
            columns=columns
        )
        return redirect('screen_dashboard')
    return render(request, 'create_screen.html', {'theatres': theatres})

@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@require_http_methods(["GET", "POST"])
def update_screen(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    theatres = Theatre.objects.all()
    if request.method == "POST":
        theatre_id = request.POST.get('theatre_id')
        theatre = Theatre.objects.get(id=theatre_id)
        screen.theatre_id = theatre
        screen.name = request.POST.get('name')
        screen.ticket_price = request.POST.get('ticket_price')
        screen.save()
        return redirect('screen_dashboard')
    return render(request, 'update_screen.html', {'screen': screen, 'theatres': theatres})

@login_required(login_url='signin')
def view_screen(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    columns_range = range(1, screen.columns + 1)
    rows_range = range(1, screen.rows + 1)

    # Convert row numbers to letters (A, B, C, etc.)
    row_labels = [string.ascii_uppercase[i] for i in range(screen.rows)]

    return render(request, 'view_screen.html', {
        'screen': screen,
        'columns_range': columns_range,
        'rows_range': rows_range,
        'row_labels': row_labels,
    })
@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
def delete_screen(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    screen.delete()
    return redirect('screen_dashboard')
