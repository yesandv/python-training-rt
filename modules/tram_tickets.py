s1 = str(input(''))
a = int(s1[0])
b = int(s1[1])
c = int(s1[2])

s2 = str(input(''))
x = int(s2[0])
y = int(s2[1])
z = int(s2[2])


if (a + b + c) == (x + y + z):
    if s2 == '999':
            s2_to_str = s2.replace('999', '000')
            print(s1 + s2_to_str)
    else:
        r = int(s2)
        r += 1
        s = str(r)
        print(s1 + s)
else:
    print(s1 + s2)
