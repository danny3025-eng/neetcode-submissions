class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

    # Pass 1: create copy nodes and build the mapping
        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

    # Pass 2: wire up next and random pointers
        current = head
        while current:
            node_map[current].next = node_map.get(current.next)
            node_map[current].random = node_map.get(current.random)
            current = current.next

        return node_map[head]