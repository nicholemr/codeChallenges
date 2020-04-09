class Solution:
    def middleNode(self, head):
        node_count = 0

        current = head

        # count number of nodes
        while current:
            node_count += 1
            current = current.next

        # return the middle
        middle = int(node_count/2)
        current = head
        for i in range(middle+1):

            if i == middle:
                return current

            current = current.next
