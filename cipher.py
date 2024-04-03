substitution_dictionary = {
    "a": "f", "b": "g", "c": "h", "d": "i", "e": "j", "f": "k", "g": "l", "h": "m", "i": "n", "j": "o", "k": "p",
    "l": "q", "m": "r", "n": "s", "o": "t", "p": "u", "q": "v", "r": "w", "s": "x",
    "t": "y", "u": "z", "v": "a", "w": "b", "x": "c","y": "d", "z": "e",
}

# plaintext input from the user
text = input("Enter a words: ")
# converts it to lowercase
text = text.lower()

# substitutes each letter according to the given substitution dictionary
crypto_text = ""
for secret in text:
    if secret in substitution_dictionary:
        secret = substitution_dictionary[secret]
    crypto_text += secret
    
#prints the resulting crypto text
print(crypto_text)