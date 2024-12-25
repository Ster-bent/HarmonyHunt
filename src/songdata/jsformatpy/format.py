#JSON File Formatter for Songs
import os
selectFile = "/workspaces/HarmonyHunt/src/songdata/jsformatpy/songs.txt"
global song
global songNames

def formfile(selectFile):
    global song
    global songNames
    num = ["0","1","2","3","4","5","6","7","8","9","."]
    with open(selectFile, encoding="utf-8") as file:
        #Line number for file is subject to change

        #! Double Check outputs and debug
            song = str(file.readlines())
            song = song.split()
            for i in range(len(song)):
                  if song[i] == "-":
                        song.pop(i)
                        print(song[i])
            print("++++++++++++++++++++")
            print(song)
    
formfile(selectFile)
print("done")