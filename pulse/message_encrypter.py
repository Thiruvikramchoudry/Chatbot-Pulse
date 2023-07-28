from cryptography.fernet import Fernet
key = b'ROpuPFaS1GLvl-6rWlQEPhKebxpYsfDH_D3f0_hzA08='
crypter = Fernet(key)


def encrypt_message(message):
    byte_string = message.encode()

    string = crypter.encrypt(byte_string)


    return str(string, 'utf8')

def decrypt_message(message):
    decrypt = crypter.decrypt(message)
    return str(decrypt,'utf8')

