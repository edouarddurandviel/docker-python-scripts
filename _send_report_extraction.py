import os
import sys
import datetime

from datetime import datetime
from assets import queries
from assets import mailSender
from assets import zipfiles
from classes import WriteFiles


def main():

    user_rows = queries.getCompanyUsers()
    if not user_rows:
        print(f"No data directory found") 
        sys.exit(1)


    current_dir = os.getcwd()
    if not current_dir:
        print(f"No current directory found") 
        sys.exit(1)
     
     
    # create date
    #############################
    date = datetime.now() 
    
    
    # write report_01/01/2026.txt
    ############################# 
    try:
        file_path, output_dir = WriteFiles.generate(user_rows, current_dir, date)
    except Exception as e:
        if e:
            print(f"{e} file could not be written") 
            sys.exit(1) 
    
     
     
    # zip to report_01/01/2026.zip
    ############################  
    if os.path.isfile(file_path):   
        try: 
            zipped_file = zipfiles.create(file_path, output_dir, date)
            
            print(zipped_file)
        except Exception as e:
            if e:
                print(f"{e} zip file could not be created")
                sys.exit(1)
        finally:
            WriteFiles.remove(file_path)
            

    if not os.path.isfile(zipped_file):
        print(f"No zipped file was created")
        sys.exit(1) 



    # send it to addresses array
    #####################################
    emails = ['to@mail-1.com', 'to@mail-2.com']
    try:
        mailSender.send_mail_with_attachment(emails, zipped_file, file_path)
    except Exception as e:
        print(f"{e} Could not send email") 
        sys.exit(1)   
          
            
                     
                      
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: %s" % e)