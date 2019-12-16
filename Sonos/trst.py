#!/home/xsisec/env/bin/activate
'/usr/bin/env python'
from soco import SoCo
my_zone1 = SoCo('192.168.1.62')

my_zone1.player_name
my_zone1.status_light= True
my_zone1.volume = 2
my_zone2 = SoCo('192.168.1.105')
my_zone3 = SoCo('192.168.1.119')
