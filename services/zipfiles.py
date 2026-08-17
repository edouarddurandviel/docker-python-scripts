
from datetime import datetime
import os
import string
from zipfile import ZipFile


def create(source: string, dest: string, date: datetime):
    
    file_name = f"report_{date.strftime('%Y_%m_%d')}.zip"
    # zip file to company_report 
    arc_name = os.path.join(dest, file_name)

    with ZipFile(arc_name, "w") as new_zip_file:
        new_zip_file.write(source, arc_name) 
        return arc_name
            
