import json
import requests


def translate(text, source_language, dest_language):
    r = requests.get(
        'http://localhost/api_call/flask_api.php?text={}&from={}&to={}'.format(
            text, source_language, dest_language))
    if r.status_code != 200:
        return ('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
