class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_nth_from_end(head, n):
    dummy = fast = slow = Node("X")
    dummy.next = head
    while n > 0:
        fast = fast.next
        n -= 1

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


def display(head):
    while head:
        print(head.val)
        head = head.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

new_head = remove_nth_from_end(head, 2)
print(display(new_head))


head = Node(1)

new_head = remove_nth_from_end(head, 1)
print(display(new_head))
