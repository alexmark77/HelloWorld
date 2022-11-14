s='Hello World'
print(s)
sb = s.encode('ascii')
print(type(sb), sb)

s='Hello Мир 世界'
print(s)
sb = s.encode('utf-8')
print(type(sb), sb)

s1 = sb.decode('utf-8')
print(type(s1), s1)
