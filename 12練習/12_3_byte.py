s = 'Hello'
print(type(s), s)

sb = b'Hello'
print(type(sb), sb)

print(s[1])
print(sb[1])

print(s[1:3])
print(sb[1:3])

for i in sb:
    print(i, end=' ')