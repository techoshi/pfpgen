from lowerExtensions import renameFileExtensionsInDirectoryToLowerCase
import json

def CreateJSONFile(baseType, layerBase):
    thisGenJSON = {
        "type": baseType,
        "folder": baseType + "/",
        "max": 500,
        "meta": [],
        "layers": [],
        "extras": {
            "tiers": [{"type": 1}]
        }
    }

    baseJSON = {
        "Object": {
            "type": [
                
            ]
        }
    }

    for layerType in layerBase:
        
        layerBase = {
            "layer": layerType["type"],
            "folder": layerType["type"] + "/",
            "options": layerType[ "options"]
        }

        thisGenJSON["layers"].append(layerBase)

    #thisGenJSON["layers"] = baseJSON

    Final = {
        "Object":{
            "types" : [thisGenJSON]
        } 
    }


    with open("src/collections/NFT Folder" + "/WTForks-" + baseType + ".json", "w") as outfile:
        outfile.write(json.dumps(Final, indent=4))


GenericFemales = [
    'Female Afro Head',
    'Female Backwards Bent Head',
    'Female Basic Head',
    'Female Cake Head',
    'Female Crown',
    'Female Curly Head',
    'Female Dread Head',
    'Female Forward Bent',
    'Female Pigtail Head',
    'Female Pizza Head',
    'Female Sweatband Head',
    'Male Afro Head',
    'Male Backwards Bent Head',
    'Male Basic Head',
    'Male Bravo Head',
    'Male Cake Head',
    'Male Crown',
    'Male Curly Head',
    'Male Dread Head',
    'Male Forward Bent',
    'Male Pizza Head',
    'Male Sweatband'
]

CurrentType = []

for thisType in GenericFemales:
    CurrentType = []
    CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Background")})
    CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Head")})
    CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Eyes")})
    CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Mouth")})
    CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Tattoo")})
    CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Clothing")})
    CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/" + thisType + "/Accessory")})
    CreateJSONFile(thisType, CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Angel/Accessory")})
CreateJSONFile("All Male", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Accessory")})
CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Christmas/Extras")})
CreateJSONFile("Female Christmas", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Devil/Accessory")})
CreateJSONFile("Female Devil", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Tattoo")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Mouth")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Accessory")})
CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Japanese/Extras")})
CreateJSONFile("Female Japanese", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Tattoo")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Mouth")})
CurrentType.append({ "type": "Space Suit", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Space/Space Suit")})
CreateJSONFile("Female Space", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Clothing")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Mouth")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Accessory")})
CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Female Thanksgiving/Extras")})
CreateJSONFile("Female Thanksgiving", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Angel/Accessory")})
CreateJSONFile("Male Angel", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Clothing")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Mouth")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Christmas/Accessory")})
CreateJSONFile("Male Christmas", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Devil/Accessory")})
CreateJSONFile("Male Devil", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Head")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Mouth")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Tattoo")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Accessory")})
CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Japanese/Extras")})
CreateJSONFile("Male Japanese", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Tattoo")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Mouth")})
CurrentType.append({ "type": "Space Suit", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Space/Space Suit")})
CreateJSONFile("Male Space", CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Background")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Eyes")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Tattoo")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Mouth")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Accessory")})
CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/NFT Folder/Male Thanksgiving/Extras")})
CreateJSONFile("Male Thanksgiving", CurrentType)