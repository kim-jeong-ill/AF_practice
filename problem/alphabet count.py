#알파벳 개수

s = input()

alphabet = [0] * 26

s = list(s) # [b, a ...]

for i in s:
    alphabet[ord(i)-97] += 1
    
for j in alphabet:
    print(j, end = ' ')