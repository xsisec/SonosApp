#!/usr/bin/env python
import soco
import json
import string
from soco.discovery import by_name

"""Spotify imports:"""
from soco.music_services import MusicService
from soco.data_structures import DidlItem,DidlResource
from soco.compat import quote_url



"""Sonos configuration"""
device = soco.discovery.any_soco()
#find device.
print('Current device found:' + str(device))

"""Spotify configuration"""
spotify = MusicService('Spotify')
album_id = "spotify:album:5qo7iEWkMEaSXEZ7fuPvC3" # <------ an album
track_id = "spotify:track:2qs5ZcLByNTctJKbhAZ9JE" # <------ a track



"""Get current speaker state"""
device_state= device.get_current_transport_info()['current_transport_state']
print("Current Speaker state:"+device_state)

"""Print current Track"""
device_current_track=device.get_current_track_info()['playlist_position']
#print(device_current_track)





response = spotify.get_media_metadata(item_id='spotify:track:5NXHXK6hOCotCF8lvGM1I0')
print(response)











#make device play.
#device.stop()
#device.stop()

#get queue
#sonos_queue=device.get_queue()

#<iframe src="https://open.spotify.com/embed/artist/5NXHXK6hOCotCF8lvGM1I0" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>

