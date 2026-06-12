import string


def enigma_light():
    """
    Encodes or decrypts a message using a simple substitution cipher.

    The function creates two dictionaries:
    one for encoding characters and one for decoding them.
    The user is prompted to enter a message and choose a mode:
    encode ('e') or decrypt ('d').

    Returns:
        str: The encoded or decrypted message.
    """
    keys = string.ascii_letters + string.punctuation + string.whitespace
    values = keys[-1] + keys[0:-1]
    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))

    msg = input("Enter your secret message quietly: ")
    while True:
        mode = input("Crypto mode: encode (e) OR decrypt (d): ").lower()

        if mode == "e":
            return "".join([dict_e[letter] for letter in msg])
        elif mode == "d":
            return "".join([dict_d[letter] for letter in msg])
        else:
            print("Invalid input. Please try again.")


print(enigma_light())
