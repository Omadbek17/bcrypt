import bcrypt


def hashing_password(raw_password):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded_password, salt)

print(hashing_password('123'))