# -*- coding: utf-8 -*-

"""
dirsnap.gist
~~~~~~~~~~~~

Uploads the given file to Gist, anonomously.
"""

import os

import requests

GIST_URL = 'https://gist.github.com/gists'
GIST_TEMPLATE = 'https://gist.github.com/raw/{0}/{1}'


def upload(path):
    """Uploads the file at the given path to gist.github.com."""

    filename = path.split(os.path.sep)[-1]

    with open(path, 'rb') as f:
        content = f.read()

    payload = {
       'file_ext[gistfile#0]': '.txt',
       'file_name[gistfile#0]': filename,
       'file_contents[gistfile#0]': content
    }

    # Send it up to GitHub.
    r = requests.post(GIST_URL, data=payload, allow_redirects=True)

    gist_id = r.url.split(os.path.sep)[-1]

    return GIST_TEMPLATE.format(gist_id, filename)