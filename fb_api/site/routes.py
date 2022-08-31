from flask import Blueprint, render_template
from flask.app import Flask
import requests
import http.client
from flask import Response
from flask import request
from flask.json import jsonify
import json

from dotenv import load_dotenv
import os
from datetime import datetime

def configure():
    load_dotenv()



site = Blueprint('site', __name__, template_folder='site_templates')


headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key':os.getenv('api_key')
    }


@site.route('/fixtures', methods=['GET','POST'])
def fixtures():
    configure()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Get EPL Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=39&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)

            data = response.json()['response']
            
            date_obj = data['fixtures']['date']
            new_date = datetime.strptime(date_obj, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')

            return render_template("fixtures.html", data=data, new_date=new_date)

        if request.form['submit_button'] == 'Get La Liga Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=140&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("fixtures.html", data=data)

        if request.form['submit_button'] == 'Get Bundesliga Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=78&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("fixtures.html", data=data)

        if request.form['submit_button'] == 'Get Serie A Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=135&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("fixtures.html", data=data)


        if request.form['submit_button'] == 'Get French Division 1 Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=61&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("fixtures.html", data=data)

        if request.form['submit_button'] == 'Get MLS Fixtures':
            
            url = "https://v3.football.api-sports.io/fixtures?next=10&league=253&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("fixtures.html", data=data)
    return render_template('fixtures.html')


@site.route('/standings', methods=['GET','POST'])
def standings():
    configure()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Get EPL Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=39&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)

    
        if request.form['submit_button'] == 'Get La Liga Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=140&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)
    

        if request.form['submit_button'] == 'Get Bundesliga Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=78&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)

        if request.form['submit_button'] == 'Get MLS Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=253&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)

        if request.form['submit_button'] == 'Get Serie A Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=135&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)

        if request.form['submit_button'] == 'Get French Division 1 Standings':
         
            url = "https://v3.football.api-sports.io/standings?league=61&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response'][0]['league']['standings'][0] 
            return render_template("standings.html", data=data)
        
    return render_template("standings.html")

@site.route('/')
def home():
    return render_template('index.html')


@site.route('/scorers', methods=['GET','POST'])
def scorers():
    configure()
    if request.method == 'POST':
        if request.form['submit_button'] == 'EPL Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=39&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)

        if request.form['submit_button'] == 'La Liga Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=140&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)

        if request.form['submit_button'] == 'Bundesliga Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=78&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)

        if request.form['submit_button'] == 'Serie A Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=135&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)

        if request.form['submit_button'] == 'French Division 1 Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=61&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)

        if request.form['submit_button'] == 'MLS Top Scorers':
            
            url = "https://v3.football.api-sports.io/players/topscorers?league=253&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("scorers.html", data=data)
    return render_template('scorers.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/assists', methods=['GET','POST'])
def assists():
    configure()
    if request.method == 'POST':
        if request.form['submit_button'] == 'EPL Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=39"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)

        if request.form['submit_button'] == 'La Liga Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=140"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)

        if request.form['submit_button'] == 'Bundesliga Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=78"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)

        if request.form['submit_button'] == 'Serie A Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=135"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)

        if request.form['submit_button'] == 'French Division 1 Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=61"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)

        if request.form['submit_button'] == 'MLS Playmakers':
            
            url = "https://v3.football.api-sports.io/players/topassists?season=2022&league=253"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("assists.html", data=data)
    return render_template('assists.html')

@site.route('/results', methods=['GET','POST'])
def results():
    configure()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Get EPL Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=39&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)

        if request.form['submit_button'] == 'Get La Liga Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=140&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)

        if request.form['submit_button'] == 'Get Bundesliga Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=78&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)

        if request.form['submit_button'] == 'Get Serie A Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=135&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)


        if request.form['submit_button'] == 'Get French Division 1 Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=61&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)

        if request.form['submit_button'] == 'Get MLS Results':
            
            url = "https://v3.football.api-sports.io/fixtures?last=10&league=253&season=2022"

            payload={}


            response = requests.request("GET", url, headers=headers, data=payload)
            
            data = response.json()['response']
            
            return render_template("results.html", data=data)
    
    return render_template('results.html')


