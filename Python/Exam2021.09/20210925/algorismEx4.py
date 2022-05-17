# week2- day4 (codekata in python)
def top_k(nums, k):
    a = 0
    b = 0
    
    for i in nums:
        #nums.count(i) : 배열에서 중복된 요소의 개수를 구함
        if nums.count(i) > a:
            a = nums.count(i)
            b = i
    return list(range(b, b+k))

print(top_k([1,1,1,2,2,3],2))