#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder
Imported modules
fabric api
dattime
"""
from fabric import task
from fabric.api import local
from datetime import datetime

@task
def do_pack():
    """ Functions to compress web static directory
    Return - none on fail
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{now}.tgz"
    archive_path = 'versions/$archive_name'
    # Create the archive
    local('mkdir -p versions/')
    result = local(f'tar -cvzf {archive_path} web_static/')

    # Check if succesful
    if result.succeeded:
        return archive_path
    return None
