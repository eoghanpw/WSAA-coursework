import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# print(doc.toprettyxml())

retrieveTags = [
     "TrainStatus",
     "TrainLatitude",
     "TrainLongitude",
     "TrainCode",
     "TrainDate",
     "PublicMessage",
     "Direction"
]

with open("lab02_trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

with open('lab02_traincsv.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)

    objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionNode in objTrainPositionNodes:
        trainCodeNode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
        traincode = trainCodeNode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(dataList)
