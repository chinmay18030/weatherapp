from flask import Flask, render_template, request
import requests
# import json to load JSON data to a python dictionary
import json

# # urllib.request to make a request to api
# import urllib.request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name mathura
        city = 'mathura'

    # your API key will come here
    api = "60ae5874353359e18d37599372a46659"

    # source contain json data from api
    source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api)

    # converting JSON data to a dictionary
    list_of_data = json.loads(source.content)

    # data for variable list_of_data
    data = {
        "cityname":city.capitalize(),
        "country_code": str(list_of_data['sys']['country']),

        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
