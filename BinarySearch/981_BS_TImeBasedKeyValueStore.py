class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.time = collections.defaultdict(list)
        self.value = collections.defaultdict(list)
        self.max = collections.defaultdict(int)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time[key].append(timestamp)
        self.value[key].append(value)
        self.max[key] = max(self.max[key], timestamp)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.time:
            return ""
        if timestamp >= self.max[key]:
            return self.value[key][-1]
        v = bisect.bisect_right(self.time[key], timestamp)
        if v:
            return self.value[key][v - 1]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)