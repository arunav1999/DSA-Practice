class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumTillNow = 0
        output = []
        for i in nums:
            sumTillNow += i
            output.append(sumTillNow)
        return output
            