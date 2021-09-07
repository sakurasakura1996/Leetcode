import sys
line = sys.stdin.readline().strip()
line = line.split(" ")
for i, word in enumerate(line):
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        line[i] = word + "pdd" + 'a' * (i+1)
    else:
        line[i] = str(word[1:] + word[0] + "pdd" + 'a' * (i + 1))

print(" ".join(line))

