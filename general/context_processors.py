from django.shortcuts import render
import requests
import datetime
import pytz

def havaproqnozu(request):
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=169544004a20911f4cefce0e4eb79c69')
    weather_data = weather.json()

    baku_tz = pytz.timezone('Asia/Baku')

    now_baku = datetime.datetime.now(baku_tz)
    saat_baku = now_baku.strftime("%H:%M")

    return {
        'weather': weather_data,
        'saat_baku': saat_baku,
    }