#! python3

def main():


	arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]]

	max_hourglass = float('-Inf')
	
	for row in range(4):
		for column in range(4):
			hour_glass = sum(arr[row][column:column+3]) + arr[row+1][column+1] + sum(arr[row+2][column:column+3])
			if hour_glass > max_hourglass:
				max_hourglass = hour_glass
	print(max_hourglass)
	'''

	# arr = [[0, -4, -6, 0, -7, -6],[-1, -2, -6, -8, -3, -1],[-8, -4, -2, -8, -8, -6],[-3, -1, -2, -5, -7, -4],[-3, -5, -3, -6, -6, -6],[-3, -6, 0, -8, -6, -7]]

	for row in range(1):
		for column in range(1):
			top_row = arr[row]
			hourglass_top = top_row[column:column+3]
			middle_row = arr[row + 1]
			middle_int = middle_row[column + 1]
			bottom_row = arr[row + 2]
			hourglass_bottom = bottom_row[column:column+3]
			hourglass_sum = sum(hourglass_top) + middle_int + sum(hourglass_bottom)
			if hourglass_sum > max_hourglass:
				max_hourglass = hourglass_sum
	print(max_hourglass)
	'''

main()