import json

class Config:
    @staticmethod
    def get():
        config = open('config.json', 'r')
        data = json.load(config)
        return data