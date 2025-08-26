"""Task 6 Time Based Key-Value Store
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key 
with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key 
if set was previously called on it and the most recent timestamp for that key prev_timestamp 
is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values,
it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order."""

class TimeMap:

    def __init__(self):
        self.TimeMapy = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMapy:
            self.TimeMapy[key] = []
        self.TimeMapy[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.TimeMapy:
            return ""

        l, r = 0, len(self.TimeMapy[key]) - 1
        closest = ""
        while l <= r:
            mid = (l + r) // 2
            if self.TimeMapy[key][mid][1] == timestamp:
                return self.TimeMapy[key][mid][0]
            if self.TimeMapy[key][mid][1] < timestamp:
                closest = self.TimeMapy[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return closest
