#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
Imported modules
local
datetime
"""
import os
from fabric.api import local
from datetime import datetime
from fabric.operations import put, run
from fabric.context_managers import cd


env.hosts = ['34.227.89.98 web-01', '107.22.144.156 web-02']
def do_deploy(archive_path):
    """
    Transfer the .tar.gz file to remote servers.
    Params:
      local_arch - path to the local archive file
      remote_server - servers to deploy the prog to
    """
    if not os.path.exists(archive_path):
        return False

    remote_server = "/tmp/"
    remote_release = "/data/web_static/releases/"
    current_dir = "/data/web_static/current"

    try:
        put(archive_path, remote_server)

        archive_name = os.path.basename(archive_path)
        folder_name = archive_filename[:-7]
        with cd(remote_server):
            run("mkdir -p {folder_name}".format(folder_name))
            run("tar -xcf {} -c {}".format(os.path.join(remote_server, archive_name), folder_name))

        run("rm {}".format(os.path.join(remote_server, archive_name)))
        sudo("rm -f {}".format(current_dir))
        sudo("ln -s {} {}".format(os.path.join(remote_release, folder_name), current_dir))
        return True

    except Exception as e:
        return False
