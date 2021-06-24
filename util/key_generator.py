import string, random, hashlib 

MAX_KEY_LENGTH = 15

letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
random_string = ''.join(random.choice(letters) for _ in range(MAX_KEY_LENGTH))
random_key = hashlib.sha256(random_string.encode('utf-8')).hexdigest()

print(random_key)
