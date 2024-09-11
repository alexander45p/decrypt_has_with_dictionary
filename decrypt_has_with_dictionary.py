import hashlib

has_file = ""

dict_file = input("enter the address of the dictionary file")

with open(dict_file,'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:

        has_calculado = hashlib.sha256(password.encode().hexdigest())

        if has_calculado == has_file:
            print("the original password is :" + password)
            break

        else:

            print("the password is not found in the dictionary")



