from django.shortcuts import render
import datetime
import sys
sys.path.append('..')
from information.models import Information
from theme.models import Theme



def main(request):
    theme = Theme.objects.all()
    info = Information.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    return render(request, 'main.html', {
        'today': nowDate,
        'info': info,
        'theme': theme,
    })
