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
    try:
        if not os.path.exists(archive_path):
            return False

        # Upload file to remote location
        put(archive_path, '/tmp/')

        # Create the destination folder, omit timestamp
        archive_name = archive_path[18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}'\
            .format(archive_name))

        # Uncompress archive
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/\
        web_static_{}'.format(archive_name, archive_name))

        # Delete archive from server
        run('sudo rm /tmp/web_static_{}.tgz'.format(archive_name))

        # move files to into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}/.format(archive_name, archive_name)')

        # Delete extra web_static directory
        run('sudo rm rf /data/web_static/current')

        # Delete pre-existing symbolic link
        run ('sudo rm -rf /data/web_static/current')

        # Re-create symbiolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(archive_name))
    except:
        return False
    return True
