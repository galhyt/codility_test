

# (k1, v1), (k2, v2) ...


class KeyVal:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


def print_lru(func):
    def _func(self, *args):
        print(f"\033[92m{func.__name__}({','.join(map(str, args))})\033[0m")
        ret = func(self, *args)
        node = self.root
        while node:
            print(f"    {node.key} ->", end=' ')
            node = node.next
        print('')
        return ret
    return _func


class Lru:
    def __init__(self, capacity):
        self.root = None
        self.last = None
        self.capacity = capacity
        self.used = 0
        self.dict = {}

    def find_key(self, key):
        if key not in self.dict:
            return None

        return self.dict[key]

    @print_lru
    def get(self, key):
        node = self.find_key(key)
        if node:
            self.make_node_last(node)
            return node.value
        return ''

    @print_lru
    def put_key(self, key, val):
        if not self.root:
            self.root = KeyVal(key, val)
            self.last = self.root
            self.used += 1
            self.dict[key] = self.root
        else:
            node = self.find_key(key)
            if not node:
                node = KeyVal(key, val)
                self.dict[key] = node
                if self.used >= self.capacity:
                    self.root = self.root.next
                    self.root.prev = None
                else:
                    self.used += 1
            else:
                node.value = val

            self.make_node_last(node)

    def make_node_last(self, node):
        if self.last.key == node.key:
            return

        orig_next = node.next
        orig_prev = node.prev

        self.last.next = node
        node.prev = self.last
        node.next = None
        self.last = node

        if self.root.key == node.key:
            self.root = orig_next
            orig_next.prev = None
        elif orig_prev and orig_next:
            orig_prev.next = orig_next
            orig_next.prev = orig_prev


if __name__ == '__main__':
    lru = Lru(4)
    lru.put_key(1, "one")
    print(f"2={lru.get(2)}")
    print(f"1={lru.get(1)}")
    lru.put_key(2, "two")
    lru.put_key(3, "three")
    lru.put_key(4, "four")
    lru.put_key(5, "five")

