#!/usr/bin/python3

from fabric.api import *
import datetime

def do_pack():
    currentTime = datetime.datetime.now()
    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}{}{}{}{}.tgz web_static".format(currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, currentTime.second))
