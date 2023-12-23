from django.shortcuts import render
import requests
import datetime
import pytz

def havaproqnozu(request):

    baku_tz = pytz.timezone('Asia/Baku')

    now_baku = datetime.datetime.now(baku_tz)
    saat_baku = now_baku.strftime("%H:%M")

    return {
        'saat_baku': saat_baku,
    }