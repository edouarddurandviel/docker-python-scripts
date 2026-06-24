from array import array
from datetime import datetime
import os
import string
  
def generate(user_rows: array, current_dir: string, date: datetime):
 
    output_dir = os.path.join(current_dir, "tmp", "extract")
    os.makedirs(output_dir, exist_ok=True)
    
    # formated 01/01/2026
    file_name = f"report_{date.strftime('%Y_%m_%d')}.txt"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        for row in user_rows:
            f.write(f"Company: {row[0]} Email: {row[1]}\n")
    
    return file_path, output_dir


def remove(generated_textfile: string):
       os.unlink(generated_textfile)
    
                
   