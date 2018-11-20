#!/usr/bin/env python3
#Playlist Entry

class PlaylistEntry:
	def __init__(self):
		self.title = ""
		self.artist = ""
		self.playCount = 0
		#constructor does nothing at the moment
	def setTitle(self, title):
		self.title = title
	def getTitle(self):
		return self.title
	def setArtist(self, artist):
		self.artist = artist
	def getArtist(self):
		return self.artist
	def setPlayCount(self, playCount):
		self.playCount = playCount
	def getPlayCount(self):
		return self.playCount
	def increasePlayCount(self):
		self.playCount = self.playCount + 1

testPlaylistEntry = PlaylistEntry()
testPlaylistEntry.setArtist("john doe")
testPlaylistEntry.setTitle("some song")
testPlaylistEntry.setPlayCount(123)
testPlaylistEntry.increasePlayCount()

print("artist name: {}".format(testPlaylistEntry.getArtist()))
print("title name: {}".format(testPlaylistEntry.getTitle()))
print("play count: {}".format(testPlaylistEntry.getPlayCount()))