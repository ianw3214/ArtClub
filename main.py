from flask import Flask
from flask import jsonify, request, send_file
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
    Returns data about a specific contest
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

@APP.route('/image/<path>')
def get_image(path):
    """
    Returns the image file at a specified path
    """
    return send_file('images/' + path, mimetype='image/gif')

@APP.route('/users/')
def users_request():
    """
    Returns the list of users
    """
    return jsonify(contest.get_users())

@APP.route('/users/<req_user>')
def user_detail_request(req_user):
    """
    Returns data about a specific user
    """
    return jsonify(contest.get_user_detail(req_user))

if __name__ == '__main__':
    APP.run()
