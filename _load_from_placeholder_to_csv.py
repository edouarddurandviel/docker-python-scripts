import sys

from assets import queries
from assets import utilsfiles

def main():
    version = queries.getVersionFromMariaDB()
    
    if version == "11.3.2-MariaDB-1:11.3.2+maria~ubu2204":
        placeholderData = queries.getDataFromJsonPlaceholder()

        utilsfiles.createDocumentationFile("readme")
        if placeholderData:
            file = utilsfiles.createCSVFile("placeholder_data_file", placeholderData)
            if file:
                queries.loadDataInMariaDB(file)
      
        else:
            raise Exception("placeholder data not found")
    else:
        raise Exception("MariaDB version does not match to: 11.3.2-MariaDB-1:11.3.2+maria~ubu2204")
        
        

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: %s" % e)
        sys.exit(1)
