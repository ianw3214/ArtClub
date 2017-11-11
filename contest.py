import uuid
import json
import os

# setup config
UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def get_contests():
    result = {'contests':[]}
    try:
        with open("contests.json") as contest_data:
            contests = json.load(contest_data)
            for contest in contests['contests']:
                data = {}
                data['id'] = contest['id']
                data['name'] = contest['name']
                data['description'] = contest['description']
                data['reward'] = contest['reward']
                result['contests'] += [data]
    except FileNotFoundError:
        open('contests.json', 'w+')
    return result

def get_contest_detail(contest_id):
    result = {}
    try:
        with open("contests.json") as contest_data:
            contests = json.load(contest_data)
            for contest in contests['contests']:
                if contest['id'] == contest_id:
                    result['name'] = contest['name']
                    result['description'] = contest['description']
                    result['reward'] = contest['reward']
                    result['entries'] = contest['entries']
    except FileNotFoundError:
            open('contests.json', 'w+')
    return result

def add_new_contest(contest_json):
    # first read the info from the existing file
    json_data = {}
    try:
        with open("contests.json") as contest_data:
            json_data = json.load(contest_data)
    except FileNotFoundError:
        json_data = {'contests':[]}
    # Then add the new data to the json data
    new_data = {}
    # Generate a new id for the contest as well
    new_data['id'] = str(uuid.uuid4())
    new_data['name'] = contest_json['name']
    new_data['description'] = contest_json['description']
    new_data['reward'] = contest_json['reward']
    new_data['entries'] = []
    json_data['contests'] += [new_data]
    with open("contests.json", "w") as contest_data:
        contest_data.write(json_data)
    return "Data successfully added."

def add_new_entry(entry_json, entry_file):
    file_name = ""
    # save the file
    if entry_file:
        file_extension = (entry_file.split('.'))[1]
        file_name = str(uuid.uuid4()) + '.' + file_extension
        entry_file.save(os.path.join(UPLOAD_FOLDER, file_name))
    # first read the info from the existing file
    json_data = {}
    try:
        with open("entries.json") as entry_data:
            json_data = json.load(entry_data)
    except FileNotFoundError:
        json_data = {'entries': []}
    # Then add the new entry data to the json data
    new_data = {}
    new_data['id'] = str(uuid.uuid4())
    new_data['contest-id'] = entry_json['contest']
    new_data['user-id'] = entry_json['user']
    new_data['image-name'] = file_name
    json_data['entries'] += [new_data]
    return "Data successfully added."

def get_users():
    result = {'users': []}
    try:
        with open("users.json") as user_data:
            users = json.load(user_data)
            for user in users['users']:
                data = {}
                data['name'] = user['name']
                data['id'] = user['id']
                result['users'] += [data]
    except FileNotFoundError:
        open('users.json', 'w+')
    return result


def get_user_detail(user_id):
    result = {}
    try:
        with open("users.json") as user_data:
            users = json.load(user_data)
            for user in users['users']:
                if user['id'] == user_id:
                    result['name'] = user['name']
                    result['id'] = user['id']
    except FileNotFoundError:
        open('users.json', 'w+')
    return result
