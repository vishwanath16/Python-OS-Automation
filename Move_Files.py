import os
import shutil 

path = "Source path"
path2 = "Destination Path"

for i in os.listdir(path):
    path3 = path+'\\'+i
    os.chdir(path3)
    for j in os.listdir(path='.'):
        if(j[-3:] == "mp4" or j[-3:] == "mkv"):
            for k in range(10, 60):
                # os.mkdir(path2+'\\'+str(k))
                if(j[0:2] == str(k)):
                    shutil.copy(j, path2+'\\'+str(k))
                
                    
            





