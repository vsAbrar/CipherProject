from ast import literal_eval

def caesar_shift(text, shift, decrypt = False):
    if decrypt:
        shift = shift * -1
    AlphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    AlphaLower = "abcdefghijklmnopqrstuvwxyz"
    #^ Strings with all characters, index 0:25, len of 26
    ciphertext = ''
    for i in range(len(text)): #For each character of text
        if text[i].isalpha():
            if text[i].isupper():
                pos = AlphaUpper.find(text[i])
                ciphertext += (AlphaUpper[(pos + shift) % 26])
#We need to know the position of the orignial character in text, and add shift to that, rather than to i
            else:
                pos = AlphaLower.find(text[i])
                ciphertext += (AlphaLower[(pos + shift) % 26])
#Mod returns remainder, ensuring that text index is always within alphabet index, and wraps around
        else:
            ciphertext += text[i]
    return(ciphertext)

#You should be able to call ceaser_shift in your vign cipher program and iterate over it with a loop
#^ ?!
#What does a cipher within a cipher look like? Consider double and triple encryption, perhaps with recursion
#add selection for user input, check for errors, etc.

A = (caesar_shift("We Live In A Twilight World 007., Ceaser", 27))
print(A)
B = (caesar_shift(A, 27, True))
print(B)

def vigenere_shift(text, key, decrypt = False):
    key = key.upper()
    keystring = list(key)
    if len(text) <= len(keystring):
        pass
    else:
        for i in range(len(text) - len(keystring)):
            keystring.append(keystring[i % len(keystring)])
    #keystring is now the same length as the text we wish to encrypt or decrypt
    AlphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #AlphaLower = "abcdefghijklmnopqrstuvwxyz"
    newtext = ''
    if decrypt:
        for char in range(len(keystring)):
            #keystring[char] corresponds to text[char]
            #
            shift = AlphaUpper.find(keystring[char])
            letter = caesar_shift(text[char] , shift, True)
            newtext += letter
        return newtext
    else:
        for char in range(len(keystring)):
            #keystring[char] corresponds to text[char]
            #
            if text[char].isalpha():
                shift = AlphaUpper.find(keystring[char])
            else:
                pass
            letter = caesar_shift(text[char] , shift)
            newtext += letter
        return newtext
            
#how do we know what text letter we are inputting?
            
#we want to call caesear cipher with 1 character of text and shift corresponding to
#current char in keystring (caesear cipher associated w/ that letter), and append the resulting
#character to a string. We want to loop over this for the amount of letters in text, for each letter
# in the text.

a = vigenere_shift("We Live In A Twilight World 007, Vigenere", "EMBER")
print(a)
b = vigenere_shift(a, "EMBER", True)
print(b)

# characters
#key2 can be any value, but key1 must be ONLY 1,3,5,7,9,11,15,17,19,21,23,25
#key1 should be coprime with m, len of alpha (26)
def affine_cipher(text, key1, key2, decrypt = False):
    modinv26 = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
    if key1 not in modinv26:
        return "Cannot execute affine_cipher, key1 must be coprime with 26"
    AlphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    AlphaLower = "abcdefghijklmnopqrstuvwxyz"
    AlphaDictUpperText = {}
    AlphaDictLowerText = {}
    AlphaDictUpperIndex = {}
    AlphaDictLowerIndex = {}
    for x in range(len(AlphaUpper)):
        AlphaDictUpperText[AlphaUpper[x]] = x
        AlphaDictLowerText[AlphaLower[x]] = x
        AlphaDictUpperIndex[x] = AlphaUpper[x]
        AlphaDictLowerIndex[x] = AlphaLower[x]
    newtext = ''
    inv = modinv26[key1]
    for i in text:
        if decrypt:
            if i in AlphaUpper:
                xval = AlphaDictUpperText[i]
                yval = ((inv * xval) - key2 ) % 26          
                newtext += AlphaDictUpperIndex[yval]
            elif i in AlphaLower:
                xval = AlphaDictLowerText[i]
                yval = ((inv * xval) - key2 ) % 26
                newtext += AlphaDictLowerIndex[yval]
            else:
                newtext += i
        else:
            if i in AlphaUpper:
                xval = AlphaDictUpperText[i]
                yval = (key1 * (xval + key2)) % 26
                newtext += AlphaDictUpperIndex[yval]
            elif i in AlphaLower:
                xval = AlphaDictLowerText[i]
                yval = (key1 * (xval + key2)) % 26
                newtext += AlphaDictLowerIndex[yval]
            else:
                newtext += i
    return newtext
    
v = affine_cipher("We Live In A Twilight World 007, Affine", 5, 7)
print(v)
c = affine_cipher(v, 5, 7, True)
print(c)

def atbash_cipher(text, decrypt = False):
    AlphaUpper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    AlphaUpperRev = AlphaUpper.copy()
    AlphaUpperRev.reverse()
    AlphaUpperDictENCRYPT = {}
    AlphaUpperDictDECRYPT = {}
    AlphaLower = list("abcdefghijklmnopqrstuvwxyz")
    AlphaLowerRev = AlphaLower.copy()
    AlphaLowerRev.reverse()
    AlphaLowerDictENCRYPT = {}
    AlphaLowerDictDECRYPT ={}
    newtext = ''
    for i in range(len(AlphaUpper)):
        AlphaUpperDictENCRYPT[AlphaUpper[i]] = AlphaUpperRev[i]
        AlphaLowerDictENCRYPT[AlphaLower[i]] = AlphaLowerRev[i]
        AlphaUpperDictDECRYPT[AlphaUpperRev[i]] = AlphaUpper[i]
        AlphaLowerDictDECRYPT[AlphaLowerRev[i]] = AlphaLower[i]
    if decrypt:
        for i in text:
            if i in AlphaUpper:
                newtext += AlphaUpperDictDECRYPT[i]
            elif i in AlphaLower:
                newtext += AlphaLowerDictDECRYPT[i]
            else:
                newtext += i
    else:
        for i in text:
            if i in AlphaUpper:
                newtext += AlphaUpperDictENCRYPT[i]
            elif i in AlphaLower:
                newtext += AlphaLowerDictENCRYPT[i]
            else:
                newtext += i
    return newtext

A = atbash_cipher("We Live In A Twilight World 007, Atbash")
print(A)
B = atbash_cipher(A, True)
print(B)


def baconian_cipher(text, decrypt = False):
    #capital letters only
    encrypt_key = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB',
        'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
        'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB',
        'S': 'BAABA', 'T': 'BAABB', 'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
        'Y': 'BBAAA', 'Z': 'BBAAB'
           }
    decrypt_key = {}
    for k, v in encrypt_key.items():
        decrypt_key[v] = k
    newtext = []
    if decrypt:
        for i in text:
            if i in decrypt_key:
                newtext.append(decrypt_key[i])
            else:
                newtext.append(i)
        newt = ''
        for i in newtext:
            newt += i
        return newt
    else:
        text = text.upper()
        for i in text:
            if i in encrypt_key:
                newtext.append(encrypt_key[i])
            else:
                newtext.append(i)
    return newtext

A = baconian_cipher("We Live In A Twilight World 007, Baconian")
print(A)
B = baconian_cipher(A, True)
print(B)

#resources:
#https://www.dcode.fr/tools-list#cryptography

def user_cipher():
    input_text = input("Enter the text you wish to encrypt or decrypt.\n")

    while True:
        crypt_type = input("Specify the type of cryption (encrypt or decrypt):\n")
        if crypt_type.lower() == 'encrypt':
            crypt_type = False
            break
        elif crypt_type.lower() == 'decrypt':
            crypt_type = True
            break
        else:
            print("Please enter a valid type (encrypt/decrypt)")
            continue

    while True:
        cipher_type = input("Possible cipher types include: Caesar, Vigenere, Affine, Atbash, Baconian. \
    Specify the type of cipher you wish to use:\n")
        if cipher_type.lower() == 'caesar':
            while True:
                try:
                    input_shift = int(input("Please enter a positive number as the shift key: "))
                    break
                except:
                    print("Please enter a valid integer")
                    continue
            print(caesar_shift(input_text, input_shift, crypt_type))
            break
        elif cipher_type.lower() == 'vigenere':
            while True:
                input_shift = input("Please enter a text string as your shift key: ")
                if input_shift.isalpha():
                    break
                else:
                    print("Please enter a valid text string")
                    continue
            print(vigenere_shift(input_text, input_shift, crypt_type))
            break
        elif cipher_type.lower() == 'affine':
            while True:
                try:
                    keyOne = int(input("Please enter a positive number coprime with 26 as the shift key: "))
                    if keyOne not in [1,3,5,7,9,11,15,17,19,21,23,25]:
                        continue
                    break
                except:
                    print("Please enter a valid integer")
                    continue
            while True:
                try:
                    keyTwo = int(input("Please enter any positive number as the shift key: "))
                    if keyTwo < 1:
                        continue
                    break
                except:
                    print("Please enter a valid integer")
                    continue
            print(affine_cipher(input_text, keyOne, keyTwo, crypt_type))
            break
        elif cipher_type.lower() == 'atbash':
            print(atbash_cipher(input_text, crypt_type))
            break
        elif cipher_type.lower() == 'baconian':
            print(baconian_cipher(literal_eval(input_text), crypt_type))
            break
        else:
            print("This cipher type is not available. Please enter one from the list.")
            continue
        break

    while True:
        again = input("Would you still like to encrypt or decrpyt text?: ")
        if again.lower() == 'no':
            print("Thank you for using this program!")
            break
        elif again.lower() == 'yes':
            user_cipher()
        else:
            print('Please enter a valid value (yes/no): ')
            continue
        
user_cipher()
