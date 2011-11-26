Dirsnap: Snapshot of a directory.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use case: I want to easily upload a given directory from a Heroku dyno for
inspection/vendoring.

Usage
-----

Simple::

    $ dirsnap /app/
    Creating snapshot...
    Uploading snapshot...
    Done!
    http://cl.ly/0a191R3K160t1w1P0N25/snapshot-app.tar.gz

Install
-------

::

    $ pip install dirsnap


Warning
-------

Be careful! This uploads the given directory to GitHub's gist, anomonously. You won't be able to delete it.