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

        #* Double Check outputs and debug
        for i in range(74):
            song = str(file.readlines(i))
            song = song.split()
            for j in range(len(num)):
                for i in range(len(song)):
                    if song[i] == num[j]:
                        song.remove(i)


            songNames = []
            songNames.append(song)
            print(song)
    
formfile(selectFile)
print("done")