import requests

url = 'http://wttr.in/{}?nTqum&lang=ru'
locations = ['London', 'svo', 'Череповец']
for loc in locations:
  response = requests.get(url.format(loc))
  response.raise_for_status()
  print(response.text)