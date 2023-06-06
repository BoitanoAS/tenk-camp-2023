import base64

def base64_kryptering(message):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    encrypted_message = base64_bytes.decode('utf-8')
    return encrypted_message

def base64_dekryptering(encrypted_message):
    encrypted_bytes = encrypted_message.encode('utf-8')
    decrypted_bytes = base64.b64decode(encrypted_bytes)
    decrypted_message = decrypted_bytes.decode('utf-8')
    return decrypted_message


def baklengs_kryptering(melding):
    return melding[::-1]

def baklengs_dekryptering(melding):
    return melding[::-1]

def krypter(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def dekrypter(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message