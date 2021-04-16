import zipfile
 
zip_file = input("Type filename (zip): ")
 
try:
    with zipfile.ZipFile(zip_file) as z:
        z.extractall()
        print("Extracted all")
except:
    print("Invalid file")
