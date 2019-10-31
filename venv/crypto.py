# Transposition Cipher

# encryption function

def scramble2Encrypt(plainText):
    evenChars = ''
    oddchars = ''
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = evenChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(sipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars - cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

        if len(oddChars) < len(evenChars):
            plainText = plainText + evenChars[-1]

            return plainText















plainText = input("What is your plainText?")
shift = input("What is the shift?")

def ceaser(plainText, shift):

    for ch in plainText:
        if ch