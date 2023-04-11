#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers,
using the function deploy:
Prototype: def deploy():
The script should take the following steps:
Call the do_pack() function and store the path of the created archive
Return False if no archive has been created
Call the do_deploy(archive_path) function,
using the new path of the new archive
Return the return value of do_deploy
All remote commands must be executed on both of web your servers
(using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
You must use this script to deploy it on your servers:
xx-web-01 and xx-web-02
"""


from datetime import datetime
from fabric.api import run, put, env, local
from os.path import exists
env.hosts = ['54.237.107.191', '100.25.177.64']


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


def do_deploy(archive_path):
    """The function prototype to deploy the created tgz final archive"""
    if exists(archive_path) is False:
        return False
    try:
        name_file = archive_path.split("/")[-1]
        extend = name_file.split(".")[0]
        path_file = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        # Make Dirrectory
        run('mkdir -p {}{}/'.format(path_file, extend))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name_file, path_file, extend))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(name_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_file, extend))
        run('rm -rf {}{}/web_static'.format(path_file, extend))
        # Delete the symbolic link
        run('rm -f /data/web_static/current')
        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path_file, extend))
        return True
    except Exception as e:
        return False


def deploy():
    """Prototype Function for Full dployment of the final archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
