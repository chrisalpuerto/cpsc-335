class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_energy_cores(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry, digit = divmod(sum_val, 10)
        current.next = ListNode(digit)
        current = current.next

    return dummy.next

# Example Usage
def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents 342
    l2 = ListNode(5, ListNode(6, ListNode(9)))  # Represents 965
    result = merge_energy_cores(l1, l2)  # Expected output: 7 -> 0 -> 3 -> 1 (1307)
    print("Merged Energy Cores:")
    print_list(result)
