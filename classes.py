class Event():
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data[key]

class Pitch():
    def __init__(self):
        self.data = {
                        "speed": 0,
                        "type:": "normal",
                        "strikebox_pos": [0,0]
                    }

    def get(self, key):
        return self.data[key]

class Hit():
    def __init__(self):
        self.data = {
                        "player": max_player, #undefined, idk how to make nice
                        "swing": True,
                        "ball": False,
                        "strike": False,
                        "foul": False,
                        "hit": True,
                        "r": 100,
                        "theta": 30, # spray angle
                    }

    def get(self, key):
        return self.data[key]

class Catch():
    def __init__(self):
        self.data = {
                        "caught": False,
                        "receiver": "LF",
                        "r": 100,
                        "theta": 30,
                }

    def get(self, key):
        return self.data[key]

class Player():
    def f(x):
        return x
