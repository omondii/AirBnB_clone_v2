#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
Imported modules
local
datetime
"""
import os
from fabric.api import *
from datetime import datetime
from fabric.operations import put, run
from fabric.context_managers import cd


env.hosts = ['34.227.89.98', '107.22.144.156']
def do_deploy(archive_path):
    """
    Transfer the .tar.gz file to remote servers.
    Params:
      archive_path - path to the local archive file
    """
    if not os.path.exists(archive_path):
        return False

    remote_server = "/tmp/"

    try:
        put(archive_path, remote_server)

        archive_name = os.path.basename(archive_path)
        folder_name = archive_name[:-7]
        remote_release = "/data/web_static/releases/web_static_{}/".format(folder_name)
        with cd(remote_server):
            run("mkdir -p {}".format(folder_name))
            run("tar -xzf {} -C {}".format(archive_name, folder_name))

        run("rm {}".format(os.path.join(remote_server, archive_name)))
        sudo("rm -f /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(remote_release))
        return True

    except Exception as e:
        return False
