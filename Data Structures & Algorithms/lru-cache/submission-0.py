class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Initialize sentinel nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move to front (most recently used)
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node and move to front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
            # Evict LRU if over capacity
            if len(self.cache) > self.capacity:
                lru = self.tail.prev  # Least recently used is right before tail
                self._remove(lru)
                del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        # Remove node from doubly-linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node) -> None:
        # Add node right after head sentinel
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node