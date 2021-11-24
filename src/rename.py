import os
from pathlib import Path
import argparse

# Get the list of all files and directories


def renameFileExtensionsInDirectoryToLowerCase(path):

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

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Female/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/All Male/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Tattoos")
            
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Space Suit")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Tattoos")



renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Tattoos")
            
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Space Suit")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Tattoos")

renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Accessories") 
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Background")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Clothing")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Eyes")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Extras")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Heads")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Mouth")
renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Tattoos")