#! python3

def main():

n = 30
x = str(bin(n))[2:]

max_consecutive_ones = 0

temp_consecutive_ones = 0
for i in x:
	if int(i) == 1:
		temp_consecutive_ones += 1
		if temp_consecutive_ones > max_consecutive_ones:
			max_consecutive_ones = temp_consecutive_ones
			
	else:
		temp_consecutive_ones = 0

print(max_consecutive_ones)

main()
