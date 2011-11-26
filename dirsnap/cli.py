# -*- coding: utf-8 -*-

"""
dirsnap.cli
~~~~~~~~~~~

The CLI for Dirsnap.
"""

import sys

from clint import args

from .archive import archive
from .gist import upload



def display_usage():
    """Obvious, no?"""
    print 'Usage: dirsnap <dir>'


def main():
    """Dirsnap entrypoint."""

    paths = args.files

    if not paths:
        display_usage()
        sys.exit(1)

    # Create temp archive.
    print >> sys.stderr, 'Creating snapshot...'
    path = archive(paths)

    # Upload temp archive to service.
    print >> sys.stderr, 'Uploading snapshot...'
    url = upload(path)
    print >> sys.stderr, 'Done! Here it is:'

    print url


    sys.exit()