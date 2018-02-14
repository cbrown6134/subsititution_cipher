alphabet = "~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "
key = "qwertyuiop[]\\asdfghjkl;'=-0987654321`zxcvbnm,./|}{POIUYTR EWQ~!@#$%^&*()_+HJKL:\"GFDSAZ?X>C<VMBN"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "Everyone was $^@%#&*? busy, so I went to the movie alone! Rock music (never) approaches at high velocity. The river stole all 473 gods."
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
