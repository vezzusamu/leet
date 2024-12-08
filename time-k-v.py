class TimeMap:

    def __init__(self):
        self._dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key] = self._dict.get(key, {})
        self._dict[key][timestamp] = value
        print(self._dict)
        

    def get(self, key: str, timestamp: int) -> str:
        dict_ret = self._dict.get(key, {})
        rec_t = -1
        for k in dict_ret.keys():
            if k <= timestamp and k > rec_t:
                rec_t = k
        return dict_ret.get(rec_t, "")