from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
import requests
import datetime


def search(request):

    url = "https://countriesnow.space/api/v0.1/countries"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    data = data['data']

    cities = []
    for singlelist in data:
        # print(singlelist['cities'])
        for city in singlelist['cities']:
            cities.append(city)
    # data = data.get('data')
    # f = open('dummy.txt', "w",  encoding="utf-8")
    # f.write(data)
    # f.close()
    # print(data)
    context = {'autocompletion_list': cities}
    return render(request, 'home.html', context)


def test(keys, values):
    return dict(zip(keys, values))


def weather(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']

        url = 'http://api.weatherapi.com/v1/forecast.json'

        params = {
            'key': 'e4e3a794b6c6401bbaf183116231703',
            'q': search_query,
            'days': '4',
        }

        data = requests.request("GET", url, params=params)

        if data.status_code == 400:
            return render(request, '400.html')

        data = data.json()
        # current day
        dt = datetime.datetime.fromtimestamp(
            data['location']['localtime_epoch'])
        day = dt.strftime('%A')
        # 4 days ahead
        # Replace with your starting date
        start_date = datetime.date(dt.year, dt.month, dt.day)

        forecast_days_name = []
        forecastdata = []
        # Loop over the next 4 days
        for i in range(1, 4):
            # Get the date of the current day
            current_date = start_date + datetime.timedelta(days=i)

            # Get the name of the current day
            day_name = current_date.strftime('%a')
            forecast_days_name.append(day_name)

        for forecast_data in data['forecast']['forecastday']:
            forecastdata.append(forecast_data['day']['avgtemp_c'])

        forecast = test(forecast_days_name, forecastdata)

    else:
        return redirect('home')

    context = {'search_query': search_query, 'data': data,
               'day': day, 'forecast': forecast}
    return render(request, 'weather.html', context)
