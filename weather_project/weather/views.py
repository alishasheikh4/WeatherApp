from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Weather
from .serializers import WeatherSerializer

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    api_key = "3ebf7b2aa3d5a7151fbfd713d1fd52f0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        return Response({'error': 'City not found or API error'}, status=response.status_code)

    data = response.json()

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'country': data['sys']['country'],
        'icon': data['weather'][0]['icon']
    }
    weather_obj = Weather.objects.create(**weather_data)

    serializer = WeatherSerializer(weather_obj)
    return Response(serializer.data)
