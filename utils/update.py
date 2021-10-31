import os
import filecmp
import shutil
import mysql.connector
from utils.create_template import create_template
from utils.upload_content import upload_content

target = "diary-today.txt"
template = "utils/template.txt"

def main():
    # Log in mysql database
    mydb = mysql.connector.connect(
        host="localhost",
        user="youruser",
        password="yourpassword"
    )

    # Check diary today status
    if not os.path.isfile(target):
        shutil.copyfile(template, target)

    # Upload content if target has been modified
    if not filecmp.cmp(target, template, shallow=False):
        upload_content(target, mydb)
        
    # TODO renew the file

    


if __name__ == "__main__":
    main()