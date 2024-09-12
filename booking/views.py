from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from showtime.models import ShowTime
from screen.models import Screen
import string


@login_required(login_url='signin')
def book_screen(request, pk):
    showtime = get_object_or_404(ShowTime, pk=pk)
    screen = showtime.screen
    columns_range = range(1, screen.columns + 1)
    rows_range = range(1, screen.rows + 1)

    # Convert row numbers to letters (A, B, C, etc.)
    row_labels = [string.ascii_uppercase[i] for i in range(screen.rows)]

    # Get all booked seats for the showtime
    booked_seats = Booking.objects.filter(showtime=showtime).values_list('seats', flat=True)
    booked_seats = [seat for sublist in booked_seats for seat in sublist]  # Flatten the list of lists

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        amount_paid = screen.ticket_price * len(selected_seats)

        Booking.objects.create(
            user=request.user,
            showtime=showtime,
            seats=selected_seats,
            amount_paid=amount_paid
        )
        return redirect('booking_success')  # Define the URL name for booking confirmation

    return render(request, 'book_screen.html', {
        'screen': screen,
        'columns_range': columns_range,
        'rows_range': rows_range,
        'row_labels': row_labels,
        'booked_seats': booked_seats,
    })


@login_required(login_url='signin')
def confirm_booking(request, showtime_id, seats):
    showtime = get_object_or_404(ShowTime, id=showtime_id)
    seats = seats.split(',')
    total_amount = len(seats) * 10.0  # Assuming each seat costs $10.0

    if request.method == 'POST':
        Booking.objects.create(
            user=request.user,
            showtime=showtime,
            seats=seats,
            amount_paid=total_amount
        )
        return redirect('booking_success')

    return render(request, 'confirm_booking.html', {
        'showtime': showtime,
        'seats': seats,
        'total_amount': total_amount,
    })


@login_required(login_url='signin')
def booking_success(request):
    return render(request, 'booking_success.html')

