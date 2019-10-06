#!/usr/bin/env python

from soco import SoCo

sonos_bridge = SoCo('192.168.1.105') #bryggan

Sonos_1 = SoCo('192.168.1.105')
#print (Sonos_1.player_name)
Sonos_2 = SoCo('192.168.1.119')
#print (Sonos_2.player_name)

if __name__ == '__main__':
    sonos = SoCo('192.168.1.62') # Pass in the IP of your Sonos speaker
    # You could use the discover function instead, if you don't know the IP

    # Pass in a URI to a media file to have it streamed through the Sonos
    # speaker
    sonos.play_uri(
        'http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')

    track = sonos.get_current_track_info()

    print (track['title'])

    sonos.pause()

    # Play a stopped or paused track
    sonos.play()