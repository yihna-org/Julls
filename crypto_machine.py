def enigma_light():
    import string

    keys = string.ascii_letters + string.punctuation + string.whitespace
    values = keys[-1] + keys[0:-1]
    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))

    msg = input("Enter your secret message quietly: ")
    mode = input("Crypto mode: encode (e) OR decrypt (d): ")

    if mode.lower() == "e":
        new_msg = "".join([dict_e[letter] for letter in msg])
    else:
        new_msg = "".join([dict_d[letter] for letter in msg])

    return new_msg


print(enigma_light())
