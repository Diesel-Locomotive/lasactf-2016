import operator

f = open('coolencrypted.txt', 'r+')
text = f.read()
frequencies = {}

for character in text:
    frequencies[character] = 0

for character in text:
    frequencies[character] += 1

print(sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True))
