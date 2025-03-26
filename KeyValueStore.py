class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = 0

        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keyStore[key][seen][-1]

# Binary Search

# from sortedcontainers import SortedDict

# class TimeMap:
#     def __init__(self):
#         self.m = defaultdict(SortedDict)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.m[key][timestamp] = value

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.m:
#             return ""
        
#         timestamps = self.m[key]
#         idx = timestamps.bisect_right(timestamp) - 1
        
#         if idx >= 0:
#             closest_time = timestamps.iloc[idx]
#             return timestamps[closest_time]
#         return ""
