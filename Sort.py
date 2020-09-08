import math

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
		# set is length of the portion of the array that is still unsorted
		# not including value being moved
		set = len(ary)-1
		while set > 0:
			# i is the index of the value being moved
			i = 0
			while i < set:
				if ary[i] > ary[i+1]:
					ary[i], ary[i+1] = ary[i+1], ary[i]
				i += 1
			set -= 1


	def mergeSort(self, ary):
		a = len(ary)
		# if array length is 1 return input
		if a <= 1:
			return ary
		# find location in array to split
		half = math.ceil(len(ary)/2)
		# get right and left sorted lists
		l = ary[:half]
		r = ary[half:]
		l = self.mergeSort(l)
		r = self.mergeSort(r)
		# fuse 2 lists together until one is empty
		il, ir = 0, 0
		ret = []
		while il < len(l) and ir < len(r):
			if r[ir] < l[il]:
				ret.append(r[ir])
				ir += 1
			else:
				ret.append(l[il])
				il += 1
		# add non empty array to end of list
		if il == len(l):
			ret = ret + r[ir:]
		else:
			ret = ret + l[il:]
		return ret