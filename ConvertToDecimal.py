import math

def ConvertToDecimal (num, base):
	sum = 0
	num = str(num)
	num = str.lower(num)
	current = 0
	l = len(num)
	for i in range(0,l):
		#Converts from ASCII back to decimal for base 11 and up.
		if (ord(num[i]) > 96):
			current = ord(num[i]) - 87
		else:
			current = ord(num[i]) - 48
		sum += current*math.pow(base, l-1-i)
	return int(sum)

print(ConvertToDecimal("8f", 16))
print(ConvertToDecimal("36", 8))