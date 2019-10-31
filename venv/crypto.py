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

def encryptMessage():
    msg = input("Enter the message to encrypt.")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)
print(encryptMessage())


def ceaserEncrpyt():
    input("message")
    if "a":print("a")
    if "b": print("f")
    if "c": print("e")
    if "b": print("f")
    if "c": print("g")

print(ceaserEncrpyt())

def ceaserCipher(val):
    input("Message")
    Encryption = ''
    for E in val:
        num = ord(E)

        if num == 122:
            newnum == 97
        elif num == 90:
            newnum = 65
        else:
            newnum = + 1
        Encryption = Encryption + chr(nerwnum)
    return Encryption

print(ceaserEncrpyt('E'))


alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaser(word):
    encoded = ""
    for ch in word:
        index = alphabet.find(ch)
        nextIndex = (index + 3) % 26
        encrypt += alphabet[nextIndex]
    return encryptMessage()

print(ceaser("how was your evening"))
print(ceaser("thats good"))
