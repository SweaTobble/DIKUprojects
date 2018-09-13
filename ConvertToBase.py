import math

def ConvertToBase (num, base):
		digits = math.ceil(math.log(num+1,base))
		arr = []
		rem = num
		digit_value = 0
		for i in range (digits-1, -1, -1):
			digit_value = int(math.pow(base, i))
			arr.append(int(rem/digit_value))
			rem %= digit_value
		for j in arr:
			#Conversion to ASCII characters for base 11 and up
			if (j > 10):
				j = j + 86
				j = chr(j)
			print (j, end="", flush=True)
		print ("\n")

ConvertToBase(5,2)
ConvertToBase(27,16)
ConvertToBase(27219,27219)