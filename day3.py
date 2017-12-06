def find_distance(target):
	loop_start = 1
	loop_end = 1
	iteration = 1
	while 42:
		if loop_start <= target <= loop_end:
			break
		loop_start = loop_end + 1
		loop_end += iteration * 8
		iteration += 1
		if iteration > 1000:
			raise Exception('oops')

	ring_elem_count = loop_end - loop_start + 1

	pos = target - loop_start
	# print pos
	pos = (pos + 1 + ring_elem_count) % ring_elem_count  # rotate ring index pos left by 1
	# print pos
	pos = pos % (ring_elem_count/4)  # make the distance side independant
	# print pos
	pos = abs((iteration - 1) - pos)
	# print pos

	distance = iteration - 1  # ring distance from center
	distance += pos

	# print (iteration, loop_start, loop_end, ring_elem_count, pos, distance, )
	return distance

"""
37						31
	17	16	15	14	13
	18	5	4	3	12
	19	6	1	2	11		53
	20	7	8	9	10
	21	22	23---> .25	26
43						49	50
							81	82


start	1	2	10	26	50	82
end		1	9	25	49	81
			+8	+16	+24 +32

1 + 2*4 + 3*4 + 4*4 + 5*4

"""

# print 'find_distance(1) = %s, expected 0' % find_distance(1)
# print 'find_distance(2) = %s, expected 1' % find_distance(2)
# print 'find_distance(3) = %s, expected 2' % find_distance(3)
# print 'find_distance(10) = %s, expected 3' % find_distance(10)
# print 'find_distance(11) = %s, expected 2' % find_distance(11)
# print 'find_distance(12) = %s, expected 3' % find_distance(12)
# print 'find_distance(23) = %s, expected 2' % find_distance(23)
# print 'find_distance(24) = %s, expected 3' % find_distance(24)
# print 'find_distance(25) = %s, expected 4' % find_distance(25)
# print 'find_distance(26) = %s, expected 5' % find_distance(26)
# print 'find_distance(49) = %s, expected 6' % find_distance(49)
# print 'find_distance(50) = %s, expected 7' % find_distance(50)
# print 'find_distance(51) = %s, expected 6' % find_distance(51)
# print 'find_distance(52) = %s, expected 5' % find_distance(52)
# print 'find_distance(53) = %s, expected 4' % find_distance(53)
# print 'find_distance(1024) = %s, expected 31' % find_distance(1024)

# assert 0 == find_distance(1) 
assert 3 == find_distance(12) 
assert 2 == find_distance(23) 
assert 31 == find_distance(1024) 
print find_distance(277678)

######################################################

matrix = [
	[0 for i in range(500)]
	for j in range(500)
]

def nsum(x, y):
	return (
		matrix[x+1][y+1] +
		matrix[x+0][y+1] +
		matrix[x-1][y+1] +
		matrix[x+1][y+0] +
		# matrix[x+0][y+0] +
		matrix[x-1][y+0] +
		matrix[x+1][y-1] +
		matrix[x+0][y-1] +
		matrix[x-1][y-1]
	)

def solve2():
	x = 250
	y = 250
	matrix[x][y] = 1
	done = 1
	# print '%s: (%s, %s) = %s' % (done, x, y, matrix[x][y])

	loop_start = 1
	loop_end = 1
	iteration = 1
	while 42:
		loop_start = loop_end + 1
		loop_end += iteration * 8
		iteration += 1
		if iteration > 10:
			raise Exception()

		ring_elem_count = loop_end - loop_start + 1

		for i in range(ring_elem_count):
			side = i / (ring_elem_count / 4)
			# print 'side %s' % side

			if i == 0:
				x += 1
			elif side == 0:
				y += 1
			elif side == 1:
				x -= 1
			elif side == 2:
				y -= 1
			elif side == 3:
				x += 1
				
			matrix[x][y] = nsum(x, y)
			done += 1
			# print '%s: (%s, %s) = %s' % (done, x, y, matrix[x][y])

			if matrix[x][y] > 277678:
				return matrix[x][y]

"""
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
"""

print solve2()
