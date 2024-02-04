from scripts import Debug

ENCODED_PASSWORD = ""
DECODED_PASSWORD = ""

def encryptPassword(DecryptedPW):
    ENCODED_PASSWORD = DecryptedPW.encode('utf-8')
    HEX_ENCODED_PASSWORD = ENCODED_PASSWORD.hex()
    Debug.log("encoded pw = " + str(HEX_ENCODED_PASSWORD))
    return HEX_ENCODED_PASSWORD

def decryptPassword(EncryptedPW):
    DECODED_PASSWORD = bytes.fromhex(EncryptedPW).decode('utf-8')
    Debug.log("decoded the password...")
    return DECODED_PASSWORD

