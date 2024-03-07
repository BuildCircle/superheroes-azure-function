import json
import azure.functions as func
import urllib3
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    http = urllib3.PoolManager()

    response = http.request('GET',
                            os.environ["data_url"],
                            retries = False)

    characters = json.loads(response.data.decode("utf-8"))

    queries = req.params

    if queries:
        hero_name = queries.get('hero')
        villain_name = queries.get('villain')

        hero = None
        villain = None
        winner = None

        for character in characters["items"]:
            if character["name"] == hero_name:
                hero = character
            if character["name"] == villain_name:
                villain = character

        winner = hero if hero["score"] >= villain["score"] else villain

    return func.HttpResponse(json.dumps(winner), status_code=200)
