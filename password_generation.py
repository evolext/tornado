import random
import pyperclip
valid_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', ':', ';', '<', '>', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

rnd_len = random.randint(12,19)


print('pass len: ' + str(rnd_len))
password = ''.join(random.sample(valid_chars, rnd_len))

print(password)

# В буфер обмена копируется
pyperclip.copy(password)
