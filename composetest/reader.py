import json
import asyncio

class Reader:
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def read_file(self, filename = 'data.txt'):
        with open('data.txt') as json_file:
            data = json.load(json_file)
        return data