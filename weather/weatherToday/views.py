from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from pprint import pprint
from .models import City
import geocoder
import requests
import datetime
from .models import City
from .forms import CityForm



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time

def ajaxer(request):
	if request.is_ajax:
		latitude = request.GET.get('Latitude')
		longitude = request.GET.get('Longitude')
		loc=latitude+","+longitude
		result = geocoder.opencage([latitude, longitude], key='088559509c004bdf968fe88db705b8a8', method='reverse')
		pprint(latitude)
		pprint(longitude)
		#print(result.city, result.state, result.country)
		# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f009f5c6a0f7ab4448e65aa4b5f3f0c5'


		
		# api.openweathermap.org/data/2.5/forecast/daily?q={city name},{country code}&cnt={cnt}

		url="http://api.apixu.com/v1/forecast.json?key=d55a672ed2ea413691694833181811&q=" +latitude +"+" +longitude +"&days=7"

		# url = 'http://api.apixu.com/v1/forecast.json?key=d55a672ed2ea413691694833181811&q={latitude}{longitude}&days=7'
		# url = 'http://api.apixu.com/v1/forecast.json?key=d55a672ed2ea413691694833181811&q=Bangalore&days=7'




		# $.getJSON("https://api.apixu.com/v1/current.json?key=32df9829b4c84bfc994230724170803&q="+lat+","+lon, function (data)


		city_weather = requests.get(url.format(result.city)).json()
		pprint(city_weather)
		
		# pprint(all_data)
		weather = {
			# 'city': city_weather['name'],
			# 'country': city_weather['sys']['country'],
			# 'temperature': city_weather['main']['temp'],
			# 'description': city_weather['weather'][0]['description'],
			# 'icon': city_weather['weather'][0]['icon'],
			# 'humidity': city_weather['main']['humidity'],
			# 'pressure': city_weather['main']['pressure'],
			# 'sunrise': time_converter(city_weather['sys']['sunrise']),
			# 'sunset': time_converter(city_weather['sys']['sunset']),
			# 'wind_speed': city_weather['wind']['speed'],
			# 'dt_txt':city_weather['list'][4]['dt_txt']


			'city': city_weather['location']['name'],
			'country': city_weather['location']['country'],
			'temperature_c': city_weather['current']['temp_c'],
			'description': city_weather['current']['condition']['text'],

			'icon': city_weather['current']['condition']['icon'],
			'humidity': city_weather['current']['humidity'],
			'pressure': city_weather['current']['pressure_in'],
			'temperature_f': city_weather['current']['temp_f'],
			'wind_speed': city_weather['current']['wind_kph'],
			'dt_txt':city_weather['location']['localtime'],
			'region':city_weather['location']['region'],

			'all_date1':city_weather['forecast']['forecastday'][1]['date'],
			'all_date2':city_weather['forecast']['forecastday'][2]['date'],
			'all_date3':city_weather['forecast']['forecastday'][3]['date'],
			'all_date4':city_weather['forecast']['forecastday'][4]['date'],
			'all_date5':city_weather['forecast']['forecastday'][5]['date'],
			'all_date6':city_weather['forecast']['forecastday'][6]['date'],



			'sunrise1':city_weather['forecast']['forecastday'][1]['astro']['sunrise'],
			'sunrise2':city_weather['forecast']['forecastday'][2]['astro']['sunrise'],
			'sunrise3':city_weather['forecast']['forecastday'][3]['astro']['sunrise'],
			'sunrise4':city_weather['forecast']['forecastday'][4]['astro']['sunrise'],
			'sunrise5':city_weather['forecast']['forecastday'][5]['astro']['sunrise'],
			'sunrise6':city_weather['forecast']['forecastday'][6]['astro']['sunrise'],


			'sunset1':city_weather['forecast']['forecastday'][1]['astro']['sunset'],
			'sunset2':city_weather['forecast']['forecastday'][2]['astro']['sunset'],
			'sunset3':city_weather['forecast']['forecastday'][3]['astro']['sunset'],
			'sunset4':city_weather['forecast']['forecastday'][4]['astro']['sunset'],
			'sunset5':city_weather['forecast']['forecastday'][5]['astro']['sunset'],
			'sunset6':city_weather['forecast']['forecastday'][6]['astro']['sunset'],



			'maxtemp1':city_weather['forecast']['forecastday'][1]['day']['maxtemp_c'],
			'maxtemp2':city_weather['forecast']['forecastday'][2]['day']['maxtemp_c'],
			'maxtemp3':city_weather['forecast']['forecastday'][3]['day']['maxtemp_c'],
			'maxtemp4':city_weather['forecast']['forecastday'][4]['day']['maxtemp_c'],
			'maxtemp5':city_weather['forecast']['forecastday'][5]['day']['maxtemp_c'],
			'maxtemp6':city_weather['forecast']['forecastday'][6]['day']['maxtemp_c'],


			'desc1':city_weather['forecast']['forecastday'][1]['day']['condition']['text'],
			'desc2':city_weather['forecast']['forecastday'][2]['day']['condition']['text'],
			'desc3':city_weather['forecast']['forecastday'][3]['day']['condition']['text'],
			'desc4':city_weather['forecast']['forecastday'][4]['day']['condition']['text'],
			'desc5':city_weather['forecast']['forecastday'][5]['day']['condition']['text'],
			'desc6':city_weather['forecast']['forecastday'][6]['day']['condition']['text'],

			'icon1':city_weather['forecast']['forecastday'][1]['day']['condition']['icon'],
			'icon2':city_weather['forecast']['forecastday'][2]['day']['condition']['icon'],
			'icon3':city_weather['forecast']['forecastday'][3]['day']['condition']['icon'],
			'icon4':city_weather['forecast']['forecastday'][4]['day']['condition']['icon'],
			'icon5':city_weather['forecast']['forecastday'][5]['day']['condition']['icon'],
			'icon6':city_weather['forecast']['forecastday'][6]['day']['condition']['icon'],









	}
	# forecast_date = {'1': {},'2': {},'3': {},'4': {},'5': {},'6': {},}
	# i = 1
	# for row in forecast_date:
	# 	forecast_date[row] = city_weather['forecast']['forecastday'][i]['date']
	# 	i += 1

	
	# dates = {

	# }


	# pprint(forecast)







	#pprint(weather)
	#return HttpResponse()
	return JsonResponse(weather)	

def home(request):	
	return render(request, 'weather.html')

def manual_weather(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'



    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list
    
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'manual_weather.html', context) #returns the manual_weather.html template



def history(request):
	

	if request.is_ajax:

		# url = ' http://api.apixu.com/v1/forecast.json?key=93df6a2f32ad4598819104725181711&q=Bangalore&days=7'
		city_weather = requests.get("http://api.apixu.com/v1/forecast.json?key=93df6a2f32ad4598819104725181711&q=Bangalore&days=7".format('93df6a2f32ad4598819104725181711', 'Bangalore'))

		# city_weather = client.getCurrentWeather(q='London')		
		pprint(city_weather)
		weather = {

			'city': city_weather['location']['name'],
			'country': city_weather['location']['country'],
			'temperature_c': city_weather['current']['temp_c'],
			'description': city_weather['current']['condition']['text'],
			'icon': city_weather['current']['condition']['icon'],
			'humidity': city_weather['current']['humidity'],

			# 'city': city_weather['city']['name'],
			# 'country': city_weather['city']['country'],
			# 'temperature': city_weather['list'][1]['main']['temp'],
			# 'description': city_weather['list'][1]['weather'][0]['description'],
			# 'icon': city_weather['list'][1]['weather'][0]['icon'],
			# 'humidity': city_weather['list'][1]['main']['humidity'],
			# 'pressure': city_weather['list'][1]['main']['pressure'],
			# 'sunrise': time_converter(city_weather['sys']['sunrise']),
			# 'sunset': time_converter(city_weather['sys']['sunset']),
			# 'wind_speed': city_weather['wind']['speed'],
			'dt_txt':city_weather['list'][4]['dt_txt']


	}
	return JsonResponse(weather)




# def get_precip(gooddate):
#     urlstart = 'http://api.wunderground.com/api/INSERT_KEY_HERE/history_'
#     urlend = '/q/Switzerland/Zurich.json'

#     url = urlstart + str(gooddate) + urlend
#     data = requests.get(url).json()
#     for summary in data['history']['dailysummary']:
#         print ','.join((gooddate,summary['date']['year'],summary['date']['mon'],summary['date']['mday'],summary['precipm'], summary['maxtempm'], summary['meantempm'],summary['mintempm']))

# if __name__ == "__main__":
#     from datetime import date
#     from dateutil.rrule import rrule, DAILY

#     a = date(2013, 1, 1)
#     b = date(2013, 12, 31)

#     for dt in rrule(DAILY, dtstart=a, until=b):
#         get_precip(dt.strftime("%Y%m%d"))




