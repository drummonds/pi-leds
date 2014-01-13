#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player

sc = Server(hostname="10.0.0.1", port=9090, username="user", password="password")
sc.connect()

print "Logged in: %s" % sc.logged_in
print "Version: %s" % sc.get_version()
print "Num players: %s" % sc.get_player_count()
print "Players: %s" % sc.get_players()

players = sc.get_players()
print ("Type of player = %s" % type(players))
for p in players:
	print "Player number %s" % p
	#sq = sc.get_player("00:11:22:33:44:55")

	print "Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (p.get_name(), p.get_mode(), p.get_time_elapsed(), p.is_connected, p.get_wifi_signal_strength())

	print p.get_track_title()
	print p.get_time_remaining()

p=sc.get_player('00:04:20:17:5b:41')
print("Current path = %s" % p.get_track_path())
with open('z.txt','w') as f:
	f.write("Current path = %s" % p.get_track_path())
	
p.playlist_play("file:///volume1/hdtl/Music/H3MusicArchive/Amazon%20MP3/Sam%20The%20Sham%20&%20The%20Pharaohs/20th%20Century%20Masters_%20The%20Millenium%20Collection_%20Best%20Of%20Sam%20The%20Sham%20&%20The%20Pharaohs/02%20-%20Lil%27%20Red%20Riding%20Hood.mp3")

p.play()
