from django.shortcuts import render
from .models import Information
import datetime


def information(request):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    info = Information.objects.all()
    return render(request, 'information/info.html', {
        'info': info,
        'today': nowDate,
    })
