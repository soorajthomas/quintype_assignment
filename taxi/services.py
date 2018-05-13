import json


class User:
    first_name = ''
    last_name = ''
    is_hipster = False

    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.is_hipster = data['is_hipster']


class Taxi:
    first_name = ''
    last_name = ''
    is_pink = False
    lat = 0.0
    long = 0.0
    on_duty = False

    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.is_pink = data['is_pink']
        self.lat = data['lat']
        self.long = data['long']


class Database:
    users = []
    taxis = []

    def __init__(self):
        with open("data.json", 'r') as data_file:
            json_data = json.load(data_file)
        if json_data:
            for user in json_data['users']:
                self.users.append(User(user))
            for taxi in json_data['taxis']:
                self.taxis.append(Taxi(taxi))

    def get_users(self):
        return self.users

    def get_taxis(self):
        return self.taxis
