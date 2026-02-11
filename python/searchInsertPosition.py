class Solution(object):
    def searchInsert(self, nums, target):
        leftindex =0
        rightindex = len(nums)-1

        while leftindex <= rightindex:
            mid =(leftindex + rightindex) //2

            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                leftindex = mid + 1
            else: rightindex = mid-1
        return leftindex

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    target =5
    print(sol.searchInsert(nums, target))