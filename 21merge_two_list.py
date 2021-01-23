class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_list(l1, l2):
    dummy = cur = Node("X")

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = Node(l1.val)
            l1 = l1.next
        else:
            cur.next = Node(l2.val)
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    if l2:
        cur.next = l2

    return dummy.next

 # [1, 2, 4], l2 = [1, 3, 4]


def display(head):
    while head:
        print(head.val)
        head = head.next


l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

new_head = merge_list(l1, l2)

print(display(new_head))
