# 반복문을 두 번 돌아 nums[i]와 nums[j]를 비교한 후, nums[i]와 nums[j]가 같으면 count + 1 해준다.
# 과반수는 nums.length / 2 한 것 보다 커야 하기 때문에 이를 변수로(majority) 지정해주고, count값과 비교한다.
# count값이 과반수(majority) 보다 크면 nums[i]를 반환한다.

# def more_than_half(nums):
# 	majority_count = len(nums)//2
# 	for num in nums:
# 		count = sum(1 for elem in nums if elem == num)
# 		if count > majority_count:
# 			return num

def more_than_half(nums):
	majority_count = len(nums)//2
	for num in nums:
		count = sum(1 for elem in nums if elem == num)
		if count > majority_count:
			return num

print(more_than_half([3,2,1]))
        
