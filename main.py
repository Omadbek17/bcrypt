import bcrypt


def hashing_password(raw_password):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded_password, salt)



new_password = input('?: ').encode('utf-8')

result = bcrypt.checkpw(new_password, hashing_password('123'))
print(result)

a = [7,17,27]
for i in a:
    print(i)
