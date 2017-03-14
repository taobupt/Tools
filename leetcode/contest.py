def checkSubarraySum( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:
        return False
    f = [0] * len(nums)
    f[0] = nums[0]
    for i in range(1, len(nums)):
        f[i] = nums[i] + f[i - 1]
    if k != 0:
        f = list(map(lambda x: x % k, f))
    s = {}
    s[0] = -1
    for i, a in enumerate(f):
        if a in s and s[a] < i - 1:
            return True
        if a not in s:
            s[a] = i

    return False

checkSubarraySum([23, 2, 6, 4, 7],6)

def minNumber(nums):
        #Write your code here
    nums=[str(x) for x in nums]
    res=sorted(nums,key=lambda x,x1:x[0]+x1[0])
    ans=''
    for xx in res:
        ans+=xx
    return ans
print(minNumber([1,2,3]))