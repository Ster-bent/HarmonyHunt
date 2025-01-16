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
        for i in range(100):
            global songNames
            songNames = file.readline(i)
            songNames = songNames.partition("-")[0]
            print(songNames)
                  
    
formfile(selectFile)
print("done")