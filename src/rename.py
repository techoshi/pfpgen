import os
from pathlib import Path

# Get the list of all files and directories
path = "src/collections/NFT Folder/All Female/Tattoos"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
#print(dir_list)


print("Files and directories in a specified path:")
for filename in dir_list:
    #print(filename)
    if not(filename.endswith(".DS_Store")):        
        f = os.path.join(path,filename)
        if os.path.isfile(f):
            #print(f)      
            p = Path(f)
            #p.rename(p.suffix.lower() + "")
            #print(p)
            fileExt = p.suffix.lower()
            newFileExt = fileExt + "TempBackup"
            #print(fileExt)
 
            p.rename(p.with_suffix(newFileExt))
            f2 = p.with_suffix(newFileExt)
            if os.path.isfile(f2):
               p2 = Path(f2)
               p2.rename(p.with_suffix(fileExt))
               print('{ "name": "' + p.name + '", "count": 320 },')
            #print(p)
            

dir_list2 = os.listdir(path)


            

