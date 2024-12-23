#JSON File Formatter for Songs
import os
selectFile = "songs.txt"

global songs

def scan_file(selectFile):
    with open(selectFile, encoding="utf-8") as file:
        songs = file.read()
        print(songs)
    
scan_file(selectFile)
print("done")