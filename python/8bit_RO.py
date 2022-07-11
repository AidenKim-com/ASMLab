def ror(num, shi): # 8bit
	num &= 0xff
	temp = num&((2**shi)-1)
	temp = temp << 8-shi
	num = num>>shi
	num |= temp
	return num
	
def rol(num, shi): # 8bit
	num&=0xff
	temp = (num&(ror((2**shi)-1, shi)))>>(8-shi)
	num = (num<<shi) & 0xff
	num |= temp
	return num