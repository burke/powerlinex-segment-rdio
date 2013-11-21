from __future__ import absolute_import
import os

def playing(pl):
    data = os.popen("osascript /Users/burke/Library/rdio.script").read().rstrip()
    if data == "":
        return None
    else:
        return data
