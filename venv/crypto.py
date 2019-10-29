# Transposition Cipher

# encryption function

def scramble2Encrypt(plainText):
    evenChars = ''
    oddchars = ''
    charCount = 0
    for ch in plainText:
        if