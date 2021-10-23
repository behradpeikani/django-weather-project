from django.shortcuts import render
from django.views import View
import urllib.request
import json

# Create your views here.

class Home(View):
    template_name = 'myapp/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        city = request.POST['city']
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=616c189c1b4d354c7bbde72c23d25cbc').read()

        data_list = json.loads(source)

        context = {
            'country_code': str(data_list['sys']['country']),
            'coordinate': str(data_list['coord']['lon']) + ', ' + str(data_list['coord']['lat']),
            'temp': str(data_list['main']['temp']) + ' °C',
            'pressure': str(data_list['main']['pressure']),
            'humidity': str(data_list['main']['humidity']),
            'main': str(data_list['weather'][0]['main']),
            'description': str(data_list['weather'][0]['description']),
            'icon': str(data_list['weather'][0]['icon']),
        }

        return render(request, self.template_name, context)