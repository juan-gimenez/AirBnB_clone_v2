#!/usr/bin/python3
"""
generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""

from os.path import isdir
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ creates a q.tgz file"""

    datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    checkifdir = isdir("versions")
    if checkifdir is False:
        # if versions is not created create it
        local("mkdir versions")
    f = "versions/web_static_{}.tgz".format(datetime)
    local("tar -cvzf {} web_static".format(f))
    # return the archive path if the archive has been correctly generated
    if not (os.path.exists(f)):
        return None
    else:
        return f
