import random
import string

char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
print (''.join(random.sample(char_set*10, 10)))