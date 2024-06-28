from passlib.context import CryptContext

context = CryptContext(
    # Alghoritm method to hash the password
    schemes =["pbkdf2_sha256"], 
    default ="pbkdf2_sha256",
    pbkdf2_sha256_default_rounds = 70000 # Total of iterations to reduce possible crackings
)

password = "name_234?-!"

cipher_password = context.hash(password)
print(cipher_password)

import hashlib

def encrypter():
    clave = str(input("Introduce la contraseña a cifrar: ")).encode('utf-8')


    sha256 = hashlib.sha256(clave).hexdigest()
    print("Hash SHA256: %s" % str(sha256))
    
print(encrypter())
