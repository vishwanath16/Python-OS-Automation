import os

path = "Path to the folder which you want to make operations in"

for i in os.listdir(path):
    path2 = path+'\\'+i
    os.chdir(path2)
    for j in os.listdir(path='.'):
        if(j[-3:] == "srt"):
            os.remove(j)
