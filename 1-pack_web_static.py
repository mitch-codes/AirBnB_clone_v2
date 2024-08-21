#!/usr/bin/python3

from fabric.api import *
import datetime

def do_pack():
    currentTime = datetime.datetime.now()
    local("tar -czvf web_static_{}{}{}{}{}.tgz web_static".format(currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, currentTime.second))
