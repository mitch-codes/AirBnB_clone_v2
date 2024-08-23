#!/usr/bin/python3

from fabric.api import *
import datetime

env.user = "ubuntu"
env.hosts = ['54.196.197.167', '54.208.35.96']

def do_pack():
    currentTime = datetime.datetime.now()
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}{}{}{}{}.tgz web_static".format(currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, currentTime.second))
        return("versions/web_static_{}{}{}{}{}.tgz".format(currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, currentTime.second))

    except:
        return None

def do_deploy(archive_path):
    try:
        file_name = archive_path[-25:-4]
        put(archive_path, "/tmp/{}.tgz".format(file_name))
        remote("tar -xzvf /tmp/{}.tgz /data/web_static/releases/{}".format(file_name, file_name))
        remote("rm /tmp/{}.tgz".format(file_name))
        remote("rm -f /data/web_static/current")
        remote("ln -s /data/web_static/releases/{} /data/web_static/current".format(file_name))
        return True
    except:
        return False

def deploy():
    archive_path = do_pack()
    if archive_path == None:
        return False
    else:
        myresult = do_deploy(archive_path)
        return myresult
