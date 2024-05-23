class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.kv.get(key)
        if not arr:
            return ""

        if timestamp < arr[0][0]:
            return ""

        l, r = 0, len(arr) - 1
        max_ts = arr[0]
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                if arr[m][0] > max_ts[0]:
                    max_ts = arr[m]
                l = m + 1
            else:
                r = m - 1

        return max_ts[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == '__main__':
    timemap = TimeMap()
    timemap.set("foo","bar",1)
    print(timemap.get("foo", 1))
    print(timemap.get("foo", 3))
    timemap.set("foo","bar2",4)
    print(timemap.get("foo", 4))
    print(timemap.get("foo", 5))
