import asyncio
from numpy import true_divide
import pandas as pd
import glob
from random import randrange, choice, choices
import string
import json
import os
import datetime
import sys
import argparse
import numpy as np

from sticher import stitch

numberToGenerate = 50
output = "src/output/"


async def MartiansGenerator():

    print('Number of arguments:', len(sys.argv), 'arguments.')

    print('Argument List:', str(sys.argv))

    parser = argparse.ArgumentParser()
    #parser.add_argument("app", help="The directory of background images.")
    parser.add_argument("run", help="The directory of background images.")
    parser.add_argument("sample", help="The directory of background images.")
    parser.add_argument("weightedMultiplier",
                        help="The directory of background images.")
    parser.add_argument(
        "startingNumber", help="The directory of background images.")
    parser.add_argument(
        "folderPath", help="The directory of background images.")
    parser.add_argument("JSONFile", help="The directory of background images.")
    parser.add_argument("x", help="The directory of background images.")
    parser.add_argument("y", help="The directory of background images.")
    parser.add_argument("amount", help="The directory of background images.")
    args = parser.parse_args()

    numberToGenerate = int(args.amount)
    if bool(args.run) == True:
        folderPath = args.folderPath  # "src/xMooneyCollection/"
        JSONFile = args.JSONFile  # "xMartiansGenerator.json"
        jsonName = JSONFile.split('.')[0]
        print(jsonName)
        totalmints = 0
        currentID = int(args.startingNumber)
        attemptedCombo = 0
        weightedMultiplier = float(args.weightedMultiplier)

        datestring = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(datestring)
        sourceFolder = output + jsonName + "." + datestring
        os.mkdir(sourceFolder)
        jsonFilesFolder = sourceFolder + "/json"
        imagesFilesFolder = sourceFolder + "/images"
        os.mkdir(jsonFilesFolder)
        stageOutput = sourceFolder + "/"

        startTime = datetime.datetime.now()
        logFile = open(stageOutput + 'log.txt', 'a+')
        genFile = open(stageOutput + 'generated.csv', 'a+')

        logFile.write("Generator Started at " + str(startTime) + "\n")

        # Open JSON File
        with open(folderPath + JSONFile) as json_file:
            jsonData = json.load(json_file)
            currentTypes = jsonData["Object"]["types"]
            print(str(len(currentTypes)) + " Unique Types")

            # Loop Through Object Types
            for martianIndex, objectTypes in enumerate(currentTypes):
                print("Current Type: " + objectTypes["type"])
                stichLayers = []
                layers = []
                weightedObjects = {}
                totalTypeMints = 0

                #print(len(currentTypes) + " Unique Types")
                # Loop Through Object Types Properties
                for propertyIndex, thisProperty in enumerate(objectTypes["properties"]):
                    print("Current: " +
                          objectTypes["type"] + " " + thisProperty["layer"])

                    gen_type_1 = []
                    gen_obj_1 = []

                    currentProperties = thisProperty
                    currentLayer = thisProperty["layer"]
                    stichLayers.append(currentLayer)
                    currentOptions = currentProperties["options"]

                    for thisOption in currentOptions:
                        gen_type_1.append(1)
                        gen_obj_1.append(thisOption["name"])
                        weightedObjects[currentLayer + "_" + thisOption["name"]
                                        ] = {"max": thisOption["count"], "minted": 0}

                    raw_data = {
                        'type_' + str(propertyIndex): gen_type_1,
                        currentLayer: gen_obj_1,
                        "folderpath": thisProperty["folder"],
                        "tesst": 0
                    }

                    temp_df = pd.DataFrame(
                        raw_data, columns=['type_' + str(propertyIndex), currentLayer])
                    temp_df_index = temp_df.set_index(
                        ['type_' + str(propertyIndex)]).rename_axis(['type'])
                    layers.append(temp_df_index)

                newUniqueDataframe = layers[0]

                # Outer Joins of Data Sets
                for index, dataFrame in enumerate(layers):
                    if index > 0:
                        newUniqueDataframe = newUniqueDataframe.join(
                            dataFrame, how='outer')

                print(str(len(newUniqueDataframe)) + " unique combinations")
                logFile.write(str(len(newUniqueDataframe)) + " of unique " +
                              objectTypes["type"] + " combinations" + "\n")
                numberToSample = float(len(newUniqueDataframe))*float(1)

                # should we sample?
                if bool(args.sample) == True:
                    uniqueDataframe = newUniqueDataframe.sample(frac=1)
                else:
                    uniqueDataframe = newUniqueDataframe

                newUniqueDataframe = None
                #allCombos = uniqueDataframe.iterrows()
                # Loop through every Sample Combination
                print("Start Loop")
                for index, row in uniqueDataframe.iterrows():
                    stichArray = []
                    comboArray = []
                    propertyMeta = {
                        "attributes" : []
                    }

                    shouldWeStich = True

                    # Check if you should create the combination
                    for layer in stichLayers:
                        tempProperty = layer + "_" + row[layer]
                        if (weightedObjects[tempProperty]["max"]*weightedMultiplier) <= weightedObjects[tempProperty]["minted"]:
                            shouldWeStich = False
                        stichArray.append(
                            folderPath + layer + "/" + row[layer] + ".png")
                        
                        propertyMeta["attributes"].append({
                            "trait_type": layer,
                            "value": row[layer]
                        })
                        comboArray.append(layer + "/" + row[layer])

                    attemptedCombo = attemptedCombo+1

                    print("---Checking Combination#:" + str(attemptedCombo))
                    if shouldWeStich == True:
                        totalmints = totalmints+1
                        currentID = currentID+1
                        totalTypeMints = totalTypeMints+1
                        #newpath = r'' + stageOutput + objectTypes["type"] + "/" + str(currentID)
                        newpath = imagesFilesFolder + "/"

                        stringCurrentID = str(currentID)
                        propertyMeta["description"] = "Friendly OpenSea Creature that enjoys long swims in the ocean."
                        propertyMeta["external_url"] = "https://openseacreatures.io/" + stringCurrentID
                        propertyMeta["image"] = "https://storage.googleapis.com/opensea-prod.appspot.com/puffs/" + stringCurrentID + ".png"
                        propertyMeta["name"] = "xMartian" + stringCurrentID

                        if not os.path.exists(newpath):
                            os.makedirs(newpath)

                        if 1 == 1:
                            asyncio.ensure_future(stitch(newpath + "/", str(currentID), stichArray, int(args.x), int(args.y)))
                            genFile.write(",".join(comboArray) + "\n")
                            # Serializing json
                            propertyMeta["combination"] = ",".join(comboArray)
                            json_object = json.dumps(propertyMeta, indent=4)

                            # Writing to sample.json
                            # str(martianIndex)
                            with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
                                outfile.write(json_object)

                        print("---Mint#:" + str(totalmints))
                        for layer in stichLayers:
                            tempProperty = layer + "_" + row[layer]
                            weightedObjects[tempProperty]["minted"] = weightedObjects[tempProperty]["minted"]+1

                        if totalmints >= numberToGenerate or totalTypeMints >= objectTypes["max"]:
                            break

                logFile.write("Generated " + str(totalTypeMints) +
                              " " + objectTypes["type"] + " combinations" + "\n")

                weightedObjectsjson_object = json.dumps(
                    weightedObjects, indent=4)
                # Writing to sample.json
                with open(stageOutput + "_" + "weightedresults.json", "w") as outfile:
                    outfile.write(weightedObjectsjson_object)

                if totalmints >= numberToGenerate:
                    break

        logFile.write("Generated " + str(totalmints) + " combinations" + "\n")
        endTime = datetime.datetime.now()
        logFile.write("Generator Ended at " + str(endTime) + "\n")
        logFile.close()


asyncio.run(MartiansGenerator())
