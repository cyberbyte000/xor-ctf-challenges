msg=bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
flag=''
for i in msg:
	k=i^16
	flag=flag+chr(k)

print(flag)
