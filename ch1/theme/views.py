from django.shortcuts import render, get_object_or_404, redirect
import datetime
from .models import Theme, Booking
from .forms import BookingForm
import sys
sys.path.append('..')
from information.models import Information


def theme(request):
    return render(request, 'theme/theme.html')


def theme_info(request):
    info = Information.objects.all()
    theme = Theme.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    return render(request, 'theme/theme_info.html', {
        'today': nowDate,
        'theme': theme,
        'info': info
    })


def theme_list(request, date):
    date = date
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])-1
    day = int(date.split('-')[2])
    booking = Booking.objects.all()
    booking = booking.filter(date=date)
    info = Information.objects.all()
    theme = Theme.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    return render(request, 'theme/theme_list.html', {
        'date': date,
        'year': year,
        'month': month,
        'day': day,
        'booking': booking,
        'today': nowDate,
        'theme': theme,
        'info': info,
    })


def theme_booking(request, date, theme):
    date = date
    year = int(date.split('-')[0])
    month = int(date.split('-')[1]) - 1
    day = int(date.split('-')[2])
    themes = Theme.objects.all()
    info = Information.objects.all()
    theme = get_object_or_404(Theme, name=theme)
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    date = date
    return render(request, 'theme/theme_booking.html', {
        'date': date,
        'year': year,
        'month': month,
        'day': day,
        'themes': themes,
        'theme': theme,
        'today': nowDate,
        'info': info,
    })


def booking_detail(request, date, theme, time):
    time = time
    date = date
    info = Information.objects.all()
    theme = get_object_or_404(Theme, name=theme)
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.theme = theme
            booking.date = date
            booking.time = time
            booking.save()
            return redirect('theme:booking_complete')
    else:
        form = BookingForm()

    return render(request, 'theme/booking_detail.html', {
        'theme': theme,
        'date': date,
        'time': time,
        'today': nowDate,
        'info': info,
        'form': form,
    })


def booking_complete(request):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    return render(request, 'theme/booking_complete.html', {
        'today': nowDate
    })