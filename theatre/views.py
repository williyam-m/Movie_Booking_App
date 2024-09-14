from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from user.views import role_required


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@login_required(login_url='signin')
def dashboard(request):
    theatre_list = Theatre.objects.all()
    return render(request, 'theatre-dashboard.html', {'theatre_list': theatre_list})


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@require_http_methods(["GET", "POST"])
def create_theatre(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        Theatre.objects.create(name=name, location=location)
        return redirect('dashboard')
    return render(request, 'create_theatre.html')


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@require_http_methods(["GET", "POST"])
def update_theatre(request, pk):
    theatre = get_object_or_404(Theatre, pk=pk)
    if request.method == "POST":
        theatre.name = request.POST.get('name')
        theatre.location = request.POST.get('location')
        theatre.save()
        return redirect('dashboard')
    return render(request, 'update_theatre.html', {'theatre': theatre})


@login_required(login_url='signin')
@role_required(['SuperAdmin', 'Admin'])
@require_http_methods(["POST"])
def delete_theatre(request, pk):
    theatre = get_object_or_404(Theatre, pk=pk)
    theatre.delete()
    return redirect('dashboard')

@login_required(login_url='signin')
def view_theatre(request, pk):
    theatre = get_object_or_404(Theatre, pk=pk)
    return render(request, 'view_theatre.html', {'theatre': theatre})
