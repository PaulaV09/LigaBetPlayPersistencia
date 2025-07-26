import json
import os
from typing import Dict, List, Optional
def readJson(fileName: str)->Dict:
    try:
        with open(fileName, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(fileName: str,  data : Dict)->Dict:
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def updateJson(fileName: str, data : Dict, path: Optional[List[str]] = None) -> None:
    currentData = readJson(fileName)
    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    
    writeJson(fileName, currentData)

def deleteJson(fileName: str, path: List[str])->bool:
    data = readJson(fileName)
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if not isinstance(current, dict) or key not in current:
            return False
        current = current[key]
    
    if path and isinstance(current, dict) and path[-1] in current:
        del current[path[-1]]
        writeJson(fileName, data)
        return True
    return False

def initializeJson(fileName: str, initialStructure:Dict)->None:
    if not os.path.isfile(fileName):
        writeJson(fileName, initialStructure)
    else:
        currentData = readJson(fileName)
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(fileName, currentData)