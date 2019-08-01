import json
import asyncio

class Dumper:
    
    data = {}
    data['people'] = []
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def append_people(self):
        data['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        data['people'].append({
            'name': 'Larry',
            'website': 'google.com',
            'from': 'Michigan'
        })
        data['people'].append({
            'name': 'Tim',
            'website': 'apple.com',
            'from': 'Alabama'
        })

    def write_file(self, filename = 'data.txt'):
        append_people()
        with open(filename, 'w') as outfile:
             json.dump(data, outfile)
