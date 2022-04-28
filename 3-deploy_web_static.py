#!/usr/bin/python3
"""
generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""

from os.path import isdir
from datetime import datetime
from fabric.operations import local, put, run
import os
from fabric.api import env
from pathlib import Path


env.hosts = ['3.92.51.75', '54.242.229.40']


def do_pack():
    """ creates a q.tgz file"""

    datet = datetime.now().strftime("%Y%m%d%H%M%S")
    checkifdir = isdir("versions")
    if checkifdir is False:
        # if versions is not created create it
        local("mkdir versions")
    f = "versions/web_static_{}.tgz".format(datet)
    local("tar -cvzf {} web_static".format(f))
    # return the archive path if the archive has been correctly generated
    if not (os.path.exists(f)):
        return None
    else:
        return f


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    path = Path(archive_path)
    existsarchpath = path.is_file()
    if existsarchpath is True:
        try:
            f = archive_path.split("/")[-1]
            nod = f.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('sudo mkdir -p {}{}/'.format(path, nod))
            run('tar -xzf /tmp/{} -C {}{}/'.format(f, path, nod))
            run('rm /tmp/{}'.format(f))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, nod))
            run('rm -rf {}{}/web_static'.format(path, nod))
            run('rm -rf /data/web_static/current')
            run('sudo ln -s {}{}/ /data/web_static/current'.format(path, nod))
            return True
            # all operations have been done correctly
        except Exception:
            return False
    else:
        return False


def deploy():
    """ creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    # no archive has been created
    if archive_path is None:
        return False
    return do_deploy(archive_path)
