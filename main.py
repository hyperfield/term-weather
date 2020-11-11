import requests

def show_weather(locations, lang):
  payload = {"nTqum":"", "lang":lang}
  url_template = 'http://wttr.in/{place}'
  for location in locations:
    response = requests.get(url_template.format(place=location), params=payload)
    response.raise_for_status()
    print(response.text)

locations = ['London', 'svo', 'Череповец']
lang = "ru"

def main():
    show_weather(locations, lang)

if __name__ == '__main__':
    main()
