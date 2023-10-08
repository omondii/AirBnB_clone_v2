#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder
Imported modules
fabric api
dattime
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to compress web static directory
    Return - none on fail
    params:
      now - time of creation
      archive_name - formated name of the out archive name
    """

    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")

        archive_name = "versions/web_static_{}.tgz".format(now)
        result = local("tar -czvf {} web_static".format(archive_name))

        print("web_static packed: {} -> {}Bytes".
              format(archive_name, result.stdout.strip()))
        return archive_name
    except Exception:
        return None
