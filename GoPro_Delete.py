import os
import shutil 

path1 = "Path where you wanna make changes"

for i in os.listdir(path1):
    if(i[-3:] == "THM" or i[-3:] =="LRV"):
        source = path1 + i
        os.remove(source)
        print("Deleted", i)

            




