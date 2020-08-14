string="label"
xor_t=13


l=[]
for i in string:
	k=(ord(i)^xor_t)
	l.append(chr(k))

print(l)
