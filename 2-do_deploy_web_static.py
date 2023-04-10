#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder/data/web_static/releases
<archive filename without extension> on the web server
Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on
the web server, linked to the new version of your code
(/data/web_static/releases/<archive filename without extension>)
"""


from fabric.api import run, put, env
from os.path import exists
env.hosts = ['54.237.107.191', '100.25.177.64']


def do_deploy(archive_path):
    """The function prototype to deploy the created tgz final archive"""
    if exists(archive_path) is False:
        return False
    try:
        name_file = archive_path.split("/")[:1]
        extend = name_file.split("-")[0]
        path_file = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        # Make Dirrectory
        run('mkdir -p {}{}'.format(path_file, extend))
        run("tar -xzf /tmp/{} -C {}{}/".format(name_file, path_file, extend))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(name_file))
        run('mv (0)(1)/web_static/* (0)(1)/'.format(path_file, extend))
        run('rm -rf {}{}/web_static'.format(path_file, extend))
        # Delete the symbolic link
        run('rm -f /data/web_static/current')
        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path_file, extend))
        return True
    except Exception as e:
        return False
