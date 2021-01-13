# l1 = [2, 4, 3], l2 = [5, 6, 4]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    cur = dummy = Node(0)

    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        cur.next = Node(carry % 10)
        cur = cur.next

        carry //= 10

    return dummy.next


def display(head):
    while head:
        print(head.val)
        head = head.next


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)


l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

head = add_two_numbers(l1, l2)
print(display(head))
