import time

import redis
from flask import Flask
import json
# from dumper import Dumper
# from reader import Reader
import asyncio
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)

@app.route('/world')
def hello_world():
    return "<h1>Hello World</h1>", 200

@app.route('/error')
def error_msg():
    return "<h1>Error</h1>", 400, {"X-Special": "Value"}

@app.route("/email")
def invalid_email ():
    return {"error": "Invalid email"}, 400

@app.route("/response")
def json_response ():
    # asyncio.run(dumper.write_file())
    # response = asyncio.run(reader.read_file())
    dumper.write_file()
    response = reader.read_file()
    # asyncio.run(response)
    obj = {u"answer": [42.2], u"abs": 42}
    # print(json.dumps(obj, indent=4))
    return obj, 200

@app.route("/json")
def json_func_write():
    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
    json_string = json.dumps(data, indent=4)
    return data

@app.route("/read")
def json_func_read():
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

@app.route("/todo")
def json_req_todo():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    return todos[2]

@app.route("/pokemon")
def json_req_graphql():
    _transport = RequestsHTTPTransport(
        url='https://graphql-pokemon.now.sh/',
        use_json=True,
    )
    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )
    query = gql("""
    {
        pokemon(name: "Pikachu") {
            attacks {
                special {
                    name
                }
            }
        }
    }
    """)
    return  client.execute(query)