import os
import zipfile

for fName in os.listdir("."):
    if os.path.isdir(fName): 
        for dirpath, dirnames, filenames in os.walk(fName):
            test_zip= zipfile.ZipFile(fName+".zip", "w")
            for filename in filenames:
                test_zip.write(os.path.join(dirpath, filename))
            test_zip.close()
