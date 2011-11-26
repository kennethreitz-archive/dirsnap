# -*- coding: utf-8 -*-

import json

import requests


url = 'https://api.github.com/gists'


payload = {
    'description': 'dirsnap catpured TIMESTAMP',
    'public': False,
    'files': {
        'filename': {
            'content': 'blah'
        }
    }
}
payload = json.dumps(payload)

r = requests.post(url, data=payload)
print r
print r.headers