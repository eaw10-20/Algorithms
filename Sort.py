class Sort:
	"""
	Heap Sort (from list)
	----------
	Notes:
	child index is as follows -
		l = 2 * parent + 1
		r = 2 * parent + 2

	parent index is -
		floor((child-1)/2)

	TODO: Heap sort from class objects

	"""
	def heapSort_array(self, nums):
		# n is the length of the input array
		n = len(nums)
		# turn our input array into a heap
		# start with parent of last value and then decriment down through index 0
		for i in range(n//2-1, -1, -1):
			self.heapify(nums, n, i)
		# sort heapified array by pulling out roots
		while n > 1:
			n -= 1
			nums[0], nums[n] = nums[n], nums[0]
			self.heapify(nums, n, 0)


	def heapify(self, nums, n, i):
		# define the root as the largest
		largest = i
		# compare index to left branch
		l = 2*i + 1
		if l < n and nums[l] > nums[i]:
			largest = l
		# compare index to right branch
		r = 2*i + 2
		if r < n and nums[r] > nums[largest]:
			largest = r
		# swap if parent not largest
		if largest != i:
			nums[largest], nums[i] = nums[i], nums[largest]
			# trickle down
			self.heapify(nums, n, largest)


	def bubbleSort(self, ary):
		set = len(ary)-1
		while set > 0:
			i = 0
			while i < set:
				if ary[i] > ary[i+1]:
					ary[i], ary[i+1] = ary[i+1], ary[i]
				i += 1
			set -= 1





ary = [32, 81, 45, 62, 90, 14, 17, 65, 39, 44, 8]
sorter = Sort()
sorter.heapSort_array(ary)
print(ary)