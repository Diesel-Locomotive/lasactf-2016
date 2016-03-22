import socket
import math


# Unigram model for letter frequencies in englishthe English alphabet (A-Z)
letter_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
                      0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                      0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
                      0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                      0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
                      0.00074]

def break_cipher(cipher_text):
    entropies = get_all_entropies(cipher_text)
    lowest_entropy = 10
    for unit in entropies:
        if unit[1] < lowest_entropy:
            lowest_entropy = unit[1]
            best_shift = unit[0]
    final_result = decrypt(cipher_text, best_shift)
    return final_result

def decrypt(encrypted_text, key):
    """Return decrypted text given encrypted text and key (shift)"""
    decrypted_text = ""
    for character in encrypted_text:
        value = ord(character)
        if (value >= 65) and (value <= 90):
            decrypted_text += chr(mod(value - 65 - key, 26) + 65) # Uppercase
        elif (value >= 97) and (value <= 122):
            decrypted_text += chr(mod(value - 97 - key, 26) + 97) # Lowercase
        else:
            decrypted_text += character
    return decrypted_text

def get_entropy(text):
    """Return entropy of given string with respect to letter frequencies"""
    total_sum = 0
    for character in text:
        value = ord(character)
        if (value >= 65) and (value <= 90):
            total_sum += math.log(letter_frequencies[value - 65])
        elif (value >= 97) and (value <= 122):
            total_sum += math.log(letter_frequencies[value - 97])
    return -total_sum/math.log(2)/len(text)

def get_all_entropies(text):
    """Return an array of 26 arrays with entropies of each shift"""
    result = []
    for i in range(0, 26):
        result.append([i, get_entropy(decrypt(text, i))])
    return result

def mod(x, y):
    return (x % y + y) % y




sock = socket.socket()
sock.connect(("web.lasactf.com", 4056)) # Make connection

while True:
    problem = sock.recv(256) # Get the problem from the server
    print ("RECIEVE: " + problem)
    answer = break_cipher(problem) # Answer the problem
    print ("SEND: " + answer)
    sock.send((answer))
