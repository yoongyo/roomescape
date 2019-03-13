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
    return render(request, 'theme/theme_info.html', {
        'today': nowDate,
        'theme': theme,
        'info': info
    })


def theme_list(request, date):
    date = date
    year = date.split('-')[0]
    month = str(int(date.split('-')[1])-1)
    day = date.split('-')[2]
    booking = Booking.objects.all()
    booking = booking.filter(date=date)
    info = Information.objects.all()
    theme = Theme.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
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
    booking = Booking.objects.all()
    booking = booking.filter(date=date, theme=theme)
    time1_hour = int(theme.time1.split(':')[0])
    time1_min = int(theme.time1.split(':')[1])
    time2_hour = int(theme.time2.split(':')[0])
    time2_min = int(theme.time2.split(':')[1])
    time3_hour = int(theme.time3.split(':')[0])
    time3_min = int(theme.time3.split(':')[1])
    time4_hour = int(theme.time4.split(':')[0])
    time4_min = int(theme.time4.split(':')[1])
    time5_hour = int(theme.time5.split(':')[0])
    time5_min = int(theme.time5.split(':')[1])
    time6_hour = int(theme.time6.split(':')[0])
    time6_min = int(theme.time6.split(':')[1])
    time7_hour = int(theme.time7.split(':')[0])
    time7_min = int(theme.time7.split(':')[1])
    time8_hour = int(theme.time8.split(':')[0])
    time8_min = int(theme.time8.split(':')[1])
    time9_hour = int(theme.time9.split(':')[0])
    time9_min = int(theme.time9.split(':')[1])
    time10_hour = int(theme.time10.split(':')[0])
    time10_min = int(theme.time10.split(':')[1])
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
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
        'booking': booking,
        'time1_hour': time1_hour,
        'time1_min': time1_min,
        'time2_hour': time2_hour,
        'time2_min': time2_min,
        'time3_hour': time3_hour,
        'time3_min': time3_min,
        'time4_hour': time4_hour,
        'time4_min': time4_min,
        'time5_hour': time5_hour,
        'time5_min': time5_min,
        'time6_hour': time6_hour,
        'time6_min': time6_min,
        'time7_hour': time7_hour,
        'time7_min': time7_min,
        'time8_hour': time8_hour,
        'time8_min': time8_min,
        'time9_hour': time9_hour,
        'time9_min': time9_min,
        'time10_hour': time10_hour,
        'time10_min': time10_min,
    })


def booking_detail(request, date, theme, time):
    time = time
    date = date
    info = Information.objects.all()
    theme = get_object_or_404(Theme, name=theme)
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
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
    return render(request, 'theme/booking_complete.html', {
        'today': nowDate
    })