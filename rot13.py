def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZZYXWVUTSRQPONMLKJIHGFEDCBA"
    ciphered = ""
    for i in message:
        if i in alphabet:
            if alphabet.index(i) <= 12:
                pos = alphabet.index(i) + 13
                i_2 = alphabet[pos]
                ciphered = ciphered + i_2
            else:
                pos = alphabet.index(i) - 13
                i_2 = alphabet[pos]
                ciphered = ciphered + i_2
        elif i in cap_alphabet:
            if cap_alphabet.index(i) <= 12:
                pos = cap_alphabet.index(i) + 13
                i_2 = cap_alphabet[pos]
                ciphered = ciphered + i_2
            else:
                pos = cap_alphabet.index(i) - 13
                i_2 = cap_alphabet[pos]
                ciphered = ciphered + i_2
        else:
            ciphered = ciphered + str(i)
    return (ciphered)

    pass
