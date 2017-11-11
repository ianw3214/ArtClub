from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
import contest
import json
APP = Flask(__name__)
CORS(APP)

@APP.route('/')
def nothing():
    """
    Return nothing for the default url
    """
    return "Not a valid URL"

@APP.route('/contests/')
def contest_request():
    """
    Return the list of contest information
    """
    return jsonify(contest.get_contests())

@APP.route('/contests/<req_contest>')
def contest_detail_request(req_contest):
    """
    Return the list of contest information
    """
    return jsonify(contest.get_contest_detail(req_contest))

@APP.route('/contests/new/', methods=['POST'])
def new_contest():
    """
    Creates a new contest and adds it to the contest list
    """
    if not request.json:
        return "No data read..."
    return contest.add_new_contest(json.dumps(request.json))

@APP.route('/entry/new/', methods=['POST'])
def new_entry():
    """
    Creates a new entry for a specific contest
    """
    if not request.json:
        return "No data read..."
    if 'entryFile' not in request.files:
        return "No file found..."
    return contest.add_new_entry(json.dumps(request.json), request.files['entryFile'])

if __name__ == '__main__':
    APP.run()
