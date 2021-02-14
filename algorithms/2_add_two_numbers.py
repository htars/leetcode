class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:

    def _node_to_integer(self, node):
        nd = node
        s = ''
        while True:
            s += str(nd.val)
            if nd.next:
                nd = nd.next
            else:
                break
        return int(s[::-1])


    def _integer_to_node(self, n):
        nodes = []
        prev_node = None        
        for c in str(n)[::-1]:
            i = int(c)
            node = ListNode(val=i)
            if prev_node is not None:
                prev_node.next = node
            prev_node = node
            nodes.append(node)
        return nodes[0]
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self._node_to_integer(l1)
        n2 = self._node_to_integer(l2)
        n3 = n1 + n2
        return self._integer_to_node(n3)


def l_to_nodes(l):
    nodes = []
    prev_node = None
    for n in l:
        node = ListNode(val=n)
        if prev_node is not None:
            prev_node.next = node
        prev_node = node
        nodes.append(node)
    return nodes


if __name__ == '__main__':
    s = Solution()

    l1 = [2, 4, 3]
    l1_nodes = l_to_nodes(l1)
    l2 = [5, 6, 4]
    l2_nodes = l_to_nodes(l2)

    node1 = l1_nodes[0]
    node2 = l2_nodes[0]

    res = s.addTwoNumbers(node1, node2)
    print(res.val)
    print(res.next.val)
