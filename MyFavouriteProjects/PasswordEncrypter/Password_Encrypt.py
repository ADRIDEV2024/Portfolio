from passlib.context import CryptContext

context = CryptContext(
    # Alghoritm method to hash the password
    schemes = ["pbkdf2_sha256"], 
    default = "pbkdf2_sha256",
    pbkdf2_sha256_default_rounds = 30000 # Total of iterations to reduce possible crackings
)

password = "myinsecurepassword_123 "

cipher_password = context.hash(password)
print(cipher_password)
