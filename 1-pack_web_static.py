#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions
(your function should create this folder if it doesn’t exist)
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if
the archive has been correctly generated. Otherwise, it should return None
"""


from datetime import datetime
from fabric.api import *


def do_pack():
    """The prototype function to use fabric to compare before sending"""
    time = datetime.now()
    new_archive = 'web_static_' + time.strftime(
                    '%Y-%m-%dT%H:%M:%S') + '.' + 'tgz'
    local('mkdir -p versions')
    create = local("tar -cvzf versions/{} web_static".format(new_archive))
    if create is not None:
        return new_archive
    else:
        return None
