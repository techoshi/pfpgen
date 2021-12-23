import glob
import json
import random
import asyncio
from sticher import stitch

def merge_JsonFiles(allFiles):
    result = []
    folder = "Female"

    for currentFile in allFiles:       

        with open(currentFile, 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
                        
            thisJson["description"] = "Stuffy Bunny Collection"
            thisJson["name"] = "Stuffy Bunny #" + theID
            thisJson["external_url"] = "https://www.stuffybunnynft.com"
            thisJson["image"] = "ipfs://QmTkDMtTEDL87A8H9c4WU3Kcj922pADS4JZNwgkDXK9rxL/" + theID + ".png"
            del thisJson['combination'] 
            del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/Stuffy Bunny/newJSON/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/Stuffy Bunny/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)