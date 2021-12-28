class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sorting according to the start time
        intervals.sort(key = lambda x:x[0])
        merged_intervals = []
        current_interval = intervals[0]
        for i in range(len(intervals)):
            if(intervals[i][0] <= current_interval[1]):
                current_interval[1] = max(current_interval[1],intervals[i][1])
            else:
                merged_intervals.append(current_interval)
                current_interval = intervals[i]
        merged_intervals.append(current_interval)
        return merged_intervals
        
        
        