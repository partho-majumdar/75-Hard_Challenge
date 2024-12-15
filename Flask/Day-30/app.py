from flask import Flask, jsonify, request
import ipl
import emni

app = Flask(__name__)


@app.route("/")
def home():
    return "This is home"


@app.route("/api/teams")
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


# http://127.0.0.1:5000/api/teamvteam?team1=Royal Challengers Bangalore&team2=Rajasthan Royals
@app.route("/api/teamvteam")
def teamvteam():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")

    response = ipl.teamVteamAPI(team1, team2)
    return jsonify(response)


@app.route("/api/team-record")
def team_record():
    team_name = request.args.get("team")
    response = emni.teamAPI(team_name)
    return response


@app.route("/api/batting-record")
def batting_record():
    batsman_name = request.args.get("batsman")
    response = emni.batsmanAPI(batsman_name)
    return response


@app.route("/api/bowling-record")
def bowling_record():
    bowler_name = request.args.get("bowler")
    response = emni.bowlerAPI(bowler_name)
    return response


app.run(debug=True)


# jsonify --> dictionary to json
# postman --> for test api
