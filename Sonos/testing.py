#!/usr/bin/env python
import os
import soco
from soco.discovery import by_name
devices = soco.discovery.any_soco()
'''my_zone2 = soco('192.168.1.105')'''
'''my_zone3 = soco('192.168.1.119')'''
devices = soco.discover ()
print(devices)
