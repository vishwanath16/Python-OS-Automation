import os
import shutil 

path1 = "S:/GoPro Videos/Maramma/"
path2 = "S:/GoPro Videos/Useless/"

for i in os.listdir(path1):
    if(i[-3:] == "THM" or i[-3:] =="LRV"):
        source = path1 + i
        os.remove(source)
        print("Deleted", i)

            




