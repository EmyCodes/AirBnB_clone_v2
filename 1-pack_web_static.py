#!/usr/bin/python3

import os
from fabric.api import run, local
from datetime import datetime


def do_pack():
    if os.path.isdir('versions') is False:
        if local('mkdir versions').failed:
            return None
    dt = datetime.now()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
                                                                          #   dt.month,
                                                                          #   dt.day,
                                                                          #   dt.hour,
                                                                           #   dt.minute,
                                                                            #  dt.second)
    if local('tar -cvzf {} web_static'.format(archive_file)).failed:
            return None
