def letterToIndex(letter):
    from string import ascil_lowercase
    alphabet = ascil_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:
        print("error:", letter, "is not in the alphabet")
        return idx

def indexToIndex(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error:", idx, "it is to large.")
    elif idx < 0:
            print("error:", idx, "it is to small.")
    else:
        letter = alphabet[idx]
    return letter
