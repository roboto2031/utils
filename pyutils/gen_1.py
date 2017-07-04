# 8 digit gen 0 - 99999999

f = open('8digit.lst', 'w');

for i in range(0,100000000):
	f.write(str(i).zfill(8)+"\n");

