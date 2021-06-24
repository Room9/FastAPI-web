import string, random, hashlib 

MAX_KEY_LENGTH = 15
AES_KEY_LENGTH = 32

letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
random_string = ''.join(random.choice(letters) for _ in range(MAX_KEY_LENGTH))
token_key = hashlib.sha256(random_string.encode('utf-8')).hexdigest()

print("TOKEN_KEY: ", token_key)

aes_key = [ random.randrange(0, 256) for _ in range(AES_KEY_LENGTH) ]

print("AES_KEY: ", aes_key)
