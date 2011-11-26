# -*- coding: utf-8 -*-
"""
dirsnap.archive
~~~~~~~~~~~~~~~

"""

import tarfile
import tempfile


def generate_filename():
    return 'snapshot.tar.gz'


def archive(paths):
    """Creates an archive from the list of given paths.
    Returns the path of the created archive.
    """

    filename = generate_filename()

    tmp = tempfile.mktemp(prefix='dirsnap-', suffix=('-' + filename))

    with tarfile.open(tmp, 'w:gz') as tar:
        for path in paths:
            tar.add(path)

    return tmp




