import json
import os
import sys
import csv

def createDocumentationFile(textFilename):
    currentDir = os.getcwd()
    try:
        filename = f"{currentDir}/tmp/csv/{textFilename}.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write("[Files] Documentation for csv file")
                   
    except OSError as e:
        if e.errno:
            print(f"[Files] {e.errno} directory and file could not be created")
            sys.exit(1)
        else:
            raise
        
def createCSVFile(csvFileName, placeholderData):
    print(placeholderData.text)
    currentDir = os.getcwd()
    filename = os.path.join(currentDir, "tmp", "csv", f"{csvFileName}.csv")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
        
    json_object = json.loads(placeholderData.text)
        
    try:
        with open(filename, "w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")    
         
            writer.writerow(["userId", "title", "completed"])
           
            for line in json_object: 
                writer.writerow([
                    line.get("userId", ""),
                    line.get("title", ""),
                    line.get("completed", "")
                ])
        
        
    except OSError as e:
        if e.errno:
            print(f"[Files] {e.errno} could not create csv file")
            sys.exit(1)
            
    finally:
        return filename