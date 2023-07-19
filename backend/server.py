from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/next_race')

def get_next_f1_race():
    url = 'http://ergast.com/api/f1/current.json'
    response = requests.get(url)
    data = response.json()

    races = data['MRData']['RaceTable']['Races']

    current_datetime = datetime.now()

    next_race_info = {}

    for race in races:
        race_date_str = race['date']
        race_time_str = race['time']
        race_datetime_str = race_date_str + ' ' + race_time_str[:-1]
        race_datetime = datetime.strptime(race_datetime_str, '%Y-%m-%d %H:%M:%S')

        if race_datetime > current_datetime:
            difference = race_datetime - current_datetime
            days = difference.days
            hours, remainder = divmod(difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            next_race_info = {
                'name': race['raceName'],
                'datetime': race_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'location': race['Circuit']['Location']['locality'] + ', ' + race['Circuit']['Location']['country'],
                'days': days,
                'hours': hours,
                'minutes': minutes,
                'seconds': seconds
            }
            break
    
    return jsonify(next_race_info)

@app.route('/standings')

def get_standings():
    url = 'http://ergast.com/api/f1/current/driverStandings.json'
    response = requests.get(url)
    data = response.json()

    standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    drivers_and_points = [{
        'driver': standing['Driver']['givenName'] + ' ' + standing['Driver']['familyName'],
        'points': standing['points']
    } for standing in standings
    ]
    
    return jsonify(drivers_and_points)

if __name__ == '__main__':
    app.run(debug=True)

