def __transform_word(original:str, count: int):
    """
    private function for transforming the str using the Vigenère cipher
    
    Params:
    original: str, the message to be transformed
    count: int, number of units to shift the message by

    Return:
    str
    """
    if ord(original) > ord('Z'): # encryption: lowercase -> uppercase
        return chr((ord(original)-ord('a')+count)%26+ord('A'))
    else: # decryption: uppercase -> lowercase
        return chr((ord(original)-ord('A')+count)%26+ord('a'))

def vigencrypt(message:str, key:str):
    """
    encrypts the message using the Vigenère cipher
    
    Params:
    message: str, the lowercase message to be encrypted
    key: str, the keyword used to encrypt the message

    Return:
    str
    """
    if not message.islower():
        raise Exception("The message to be encrypted should be in lowercase letters only")
    if not key.isupper():
        raise Exception("The keywords should be in uppercase letters only")
        
    if len(message) < len(key):
        key = key[:len(message)]
    else:
        key = key*int(len(message)/len(key)) + key[:len(message)%len(key)]
    output = ""
    for i in range(len(message)):
        output += __transform_word(message[i], ord(key[i]) - ord("A"))
    return output

def vigdecrypt(message:str, key:str):
    """
    decrypt the message using the Vigenère cipher
    
    Params:
    message: str, the uppercase message to be decrypted
    key: str, the keyword used to decrypt the message

    Return:
    str
    """
    if not message.isupper():
        raise Exception("The message to be decrypted should be in uppercase letters only")
    if not key.isupper():
        raise Exception("The keywords should be in uppercase letters only")
    
    if len(message) < len(key):
        key = key[:len(message)]
    else:
        key = key*int(len(message)/len(key)) + key[:len(message)%len(key)]
    output = ""
    for i in range(len(message)):
        output += __transform_word(message[i], -(ord(key[i]) - ord("A")))
    return output